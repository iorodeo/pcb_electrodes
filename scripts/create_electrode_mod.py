from __future__ import print_function
import scipy

class ElectrodeModuleMaker(object):

    def __init__(self,param):
        self.param = param
        self.template_lines = []
        self.module_lines = []

    def run(self):
        self.load_template()
        self.module_lines = list(self.template_lines)
        self.add_ref_elect()
        self.add_wrk_elect()
        self.add_ctr_elect()
        self.write_module()

    def load_template(self):
        with open(param['module_template'],'r') as f:
            self.template_lines = f.readlines()
        self.template_lines = [line.strip() for line in self.template_lines]

    def find_end_module_index(self):
        index = -1
        for i,line in enumerate(self.module_lines):
            if '$EndMODULE' in line:
                index = i
                break
        return index

    def add_ref_elect(self):
        end_module_index = self.find_end_module_index()
        module_lines_new = self.module_lines[:end_module_index]
        ref_elect_lines = self.create_ref_elect()
        module_lines_new.extend(ref_elect_lines)
        module_lines_new.extend(self.module_lines[end_module_index:])
        self.module_lines = module_lines_new

    def create_ref_elect(self):
        elect_param = self.param['reference_electrode']
        pin = elect_param['pin']
        radius = elect_param['radius']
        radial_pos = elect_param['radial_pos']
        angle = elect_param['angle']
        angle_rad = deg_to_rad(angle)
        x_pos = radial_pos*scipy.cos(-angle_rad)
        y_pos = radial_pos*scipy.sin(-angle_rad)
        elect_lines = []
        elect_lines.append('$PAD')
        elect_lines.append('Sh "{0}" C {1:1.3f} {1:1.3f} 0 0 {2}'.format(pin, in_to_mm(2.0*radius),-int(10*angle)))
        elect_lines.append('Dr 0 0 0')
        elect_lines.append('At SMD N 00888000')
        elect_lines.append('Ne 0 ""')
        elect_lines.append('Po {0:1.3f} {1:1.3f}'.format(in_to_mm(x_pos), in_to_mm(y_pos)))
        elect_lines.append('$EndPAD')
        return elect_lines

    def add_wrk_elect(self):
        end_module_index = self.find_end_module_index()
        module_lines_new = self.module_lines[:end_module_index]
        wrk_elect_lines = self.create_wrk_elect()
        module_lines_new.extend(wrk_elect_lines)
        module_lines_new.extend(self.module_lines[end_module_index:])
        self.module_lines = module_lines_new

    def create_wrk_elect(self):
        elect_param = self.param['working_electrode']
        pin = elect_param['pin']
        radius = elect_param['radius']
        elect_lines = []
        elect_lines.append('$PAD')
        elect_lines.append('Sh "{0}" C {1:1.3f} {1:1.3f} 0 0 0'.format(pin, in_to_mm(2.0*radius)))
        elect_lines.append('Dr 0 0 0')
        elect_lines.append('At SMD N 00888000')
        elect_lines.append('Ne 0 ""')
        elect_lines.append('Po 0 0')
        elect_lines.append('$EndPAD')
        return elect_lines

    def add_ctr_elect(self):
        end_module_index = self.find_end_module_index()
        module_lines_new = self.module_lines[:end_module_index]
        ctr_elect_lines = self.create_ctr_elect()
        module_lines_new.extend(ctr_elect_lines)
        module_lines_new.extend(self.module_lines[end_module_index:])
        self.module_lines = module_lines_new

    def create_ctr_elect(self):
        elect_param = param['counter_electrode']

        radial_pos = elect_param['radial_pos']
        min_angle = elect_param['angle_range'][0]
        max_angle = elect_param['angle_range'][1]
        thickness = elect_param['thickness']
        num_segments = elect_param['segments']
        pin = elect_param['pin']
        arc_oversize = elect_param['arc_oversize']

        min_angle_rad = deg_to_rad(min_angle)
        max_angle_rad = deg_to_rad(max_angle)
        delta_angle_rad = max_angle_rad - min_angle_rad
        arc_length = radial_pos*delta_angle_rad/float(num_segments)

        height = thickness
        width =  arc_oversize*arc_length

        angle_list = -1.0*scipy.linspace(min_angle_rad, max_angle_rad, num_segments)
        x_pos_list = [radial_pos*scipy.cos(ang) for ang in angle_list] 
        y_pos_list = [radial_pos*scipy.sin(ang) for ang in angle_list] 

        elect_lines = []

        for ang, x_pos, y_pos in zip(angle_list,x_pos_list,y_pos_list):
            ang_deg = rad_to_deg(ang)
            elect_lines.append('$PAD')
            elect_lines.append('Sh "{0}" R {1:1.3f} {2:1.3f} 0 0 {3}'.format(pin,in_to_mm(height),in_to_mm(width),-int(10*ang_deg)))
            elect_lines.append('Dr 0 0 0')
            elect_lines.append('At SMD N 00888000')
            elect_lines.append('Ne 0 ""')
            elect_lines.append('Po {0:1.4f} {1:1.4f}'.format(in_to_mm(x_pos),in_to_mm(y_pos)))
            elect_lines.append('$EndPAD')

        return elect_lines

    def print_template(self):
        for line in self.template_lines:
            print(line)

    def print_module(self):
        for line in self.module_lines:
            print(line)

    def write_module(self):
        with open(self.param['output_file'],'w') as f:
            for line in self.module_lines:
                f.write('{0}\n'.format(line))


# Utility functions
# ---------------------------------------------------------------------------
def deg_to_rad(val):
    return val*scipy.pi/180.0

def rad_to_deg(val):
    return val*180.0/scipy.pi

def in_to_mm(val):
    return val*25.4

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    #working_electrode_radius = 0.05
    working_electrode_radius = 0.1

    param = {
            'module_template':  'template_ELECTRODE.mod',
            'working_electrode': {
                'pin': 2,
                'radius': working_electrode_radius, 
                },
            'reference_electrode': {
                'pin': 1,
                'radius': 0.15*working_electrode_radius,
                'radial_pos': 1.414*working_electrode_radius ,
                'angle': 135,
                },
            'counter_electrode' : {
                'pin': 3,
                'radial_pos': 1.7*working_electrode_radius,
                'angle_range': (-160,90),
                'thickness': 0.6*working_electrode_radius,
                'segments': 100,
                'arc_oversize': 1.5,
                },
            'output_file': 'ELECTRODE.mod',
            }

    maker = ElectrodeModuleMaker(param)
    maker.run()



