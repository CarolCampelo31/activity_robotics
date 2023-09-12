import sim
from niryoobject import NiryoObject

JOINTS_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6', 'joint_left', 'joint_right']
AUX_OBJECTS_NAMES = ['base_link_visual', 'edo_tip', 'edo_target', 'Sphere']


class NiryoRobot(NiryoObject):
    def __init__(self, client_id):
        super().__init__()
        self.client_id = client_id

        # robot objects
        self.base = NiryoObject()
        self.J1 = NiryoObject()
        self.J2 = NiryoObject()
        self.J3 = NiryoObject()
        self.J4 = NiryoObject()
        self.J5 = NiryoObject()
        self.J6 = NiryoObject()

        self.JL = NiryoObject()
        self.JR = NiryoObject()

        self.target = NiryoObject()
        self.tip = NiryoObject()
        self.sphere = NiryoObject()

    def _get_object_handle(self, handle_name):
        return sim.simxGetObjectHandle(self.client_id, handle_name, sim.simx_opmode_blocking)[1]

    def _get_object_position(self, object_handle, operation_mode=sim.simx_opmode_buffer):
        ret, pos = sim.simxGetObjectPosition(self.client_id, objectHandle=object_handle,
                                             relativeToObjectHandle=-1, operationMode=operation_mode)
        return pos

    def _get_relative_position(self, object_handle, operation_mode=sim.simx_opmode_oneshot_wait):
        ret, rel_pos = sim.simxGetObjectPosition(self.client_id, objectHandle=object_handle,
                                                 relativeToObjectHandle=self.base.handle, operationMode=operation_mode)
        return rel_pos

    def define_objects_names(self):
        # Define Objects Names
        self.base.name = AUX_OBJECTS_NAMES[0]
        self.tip.name = AUX_OBJECTS_NAMES[1]
        self.target.name = AUX_OBJECTS_NAMES[2]
        self.sphere.name = AUX_OBJECTS_NAMES[3]
        # Define Joints Names
        self.J1.name = JOINTS_NAMES[0]
        self.J2.name = JOINTS_NAMES[1]
        self.J3.name = JOINTS_NAMES[2]
        self.J4.name = JOINTS_NAMES[3]
        self.J5.name = JOINTS_NAMES[4]
        self.J6.name = JOINTS_NAMES[5]
        self.JL.name = JOINTS_NAMES[6]
        self.JR.name = JOINTS_NAMES[7]

    def test(self):
        for i in range(20):
            result = sim.simxGetObjectGroupData(self.client_id, sim.sim_object_joint_type,
                                                i, sim.simx_opmode_oneshot_wait)

    def define_objects_handle(self):
        err, handles, ints, floats, strings = sim.simxGetObjectGroupData(self.client_id,
                                                                         sim.sim_object_joint_type, 0,
                                                                         sim.simx_opmode_oneshot_wait)
        # Defining Joints
        for object_name, object_param in zip(strings, handles):
            if object_name == self.J1.name:
                self.J1.handle = object_param
            elif object_name == self.J2.name:
                self.J2.handle = object_param
            elif object_name == self.J3.name:
                self.J3.handle = object_param
            elif object_name == self.J4.name:
                self.J4.handle = object_param
            elif object_name == self.J5.name:
                self.J5.handle = object_param
            elif object_name == self.J6.name:
                self.J6.handle = object_param
            elif object_name == self.JL.name:
                self.JL.handle = object_param
            elif object_name == self.JR.name:
                self.JR.handle = object_param

        # Define Dummys
        err, handles, ints, floats, strings = sim.simxGetObjectGroupData(self.client_id,
                                                                         sim.sim_object_dummy_type, 0,
                                                                         sim.simx_opmode_oneshot_wait)
        for object_name, object_param in zip(strings, handles):
            if object_name == self.target.name:
                self.target.handle = object_param
            elif object_name == self.tip.name:
                self.tip.handle = object_param

        # self.base.handle = sim.simxGetObjectHandle(self.client_id, self.base.name, sim.simx_opmode_oneshot_wait)[1]

        # self.sphere.handle = sim.simxGetObjectHandle(self.client_id, self.sphere.name, sim.simx_opmode_oneshot_wait)[1]

    def get_objects_pos(self, op_mode=sim.simx_opmode_oneshot_wait):
        # set joints position
        self.J1.pos = self._get_object_position(self.J1.handle, op_mode)
        self.J2.pos = self._get_object_position(self.J2.handle, op_mode)
        self.J3.pos = self._get_object_position(self.J3.handle, op_mode)
        self.J4.pos = self._get_object_position(self.J4.handle, op_mode)
        self.J5.pos = self._get_object_position(self.J5.handle, op_mode)
        self.J6.pos = self._get_object_position(self.J6.handle, op_mode)
        # self.JL.pos = self._get_object_position(self.JL.handle, op_mode)
        # self.JR.pos = self._get_object_position(self.JR.handle, op_mode)

        # set objects positions
        # self.base.pos = self._get_object_position(self.base.handle, op_mode)
        # self.target.pos = self._get_object_position(self.target.handle, op_mode)
        # self.tip.pos = self._get_object_position(self.tip.handle, op_mode)
        # self.sphere.pos = self._get_object_position(self.sphere.handle, op_mode)

    def get_objects_rel_pos(self, op_mode=sim.simx_opmode_oneshot):

        # set joints relative position
        self.J1.rel_pos = self._get_relative_position(self.J1.handle, op_mode)
        self.J2.rel_pos = self._get_relative_position(self.J2.handle, op_mode)
        self.J3.rel_pos = self._get_relative_position(self.J3.handle, op_mode)
        self.J4.rel_pos = self._get_relative_position(self.J4.handle, op_mode)
        self.J5.rel_pos = self._get_relative_position(self.J5.handle, op_mode)
        self.J6.rel_pos = self._get_relative_position(self.J6.handle, op_mode)
        # self.JL.rel_pos = self._get_relative_position(self.JL.handle, op_mode)
        # self.JR.rel_pos = self._get_relative_position(self.JR.handle, op_mode)

        # set objects relative position
        self.target.rel_pos = self._get_relative_position(self.target.handle, op_mode)
        self.tip.rel_pos = self._get_relative_position(self.tip.handle, op_mode)

    def mov_cartesian(self, x, y, z, op_mode=sim.simx_opmode_oneshot):
        # mover para posição
        position = [x, y, z]
        print(position)

        sim.simxSetObjectPosition(self.client_id, self.sphere.handle, -1, position, op_mode)
        sim.simxSetIntegerSignal(self.client_id, 'is_inverse', 1, sim.simx_opmode_oneshot)

    def mov_joints_pos(self, t1, t2, t3, t4, t5, t6):
        sim.simxSetIntegerSignal(self.client_id, 'is_inverse', 0, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J1.handle, t1 * 3.1415 / 180, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J2.handle, t2 * 3.1415 / 180, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J3.handle, t3 * 3.1415 / 180, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J4.handle, t4 * 3.1415 / 180, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J5.handle, t5 * 3.1415 / 180, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(self.client_id, self.J6.handle, t6 * 3.1415 / 180, sim.simx_opmode_oneshot)

    # def mov_gripper(self, t_left, t_right):
    #     sim.simxSetJointTargetPosition(self.client_id, self.JL.handle, t_left * 3.1415 / 180, sim.simx_opmode_oneshot)
    #     sim.simxSetJointTargetPosition(self.client_id, self.JR.handle, t_right * 3.1415 / 180, sim.simx_opmode_oneshot)

    def mov_to_default_pos(self):
        self.mov_joints_pos(0, 0, 0, 0, 0, 0)

    def mov_cancel(self):
        pass

    def init(self):
        self.define_objects_names()
        self.define_objects_handle()
        self.get_objects_pos(op_mode=sim.simx_opmode_oneshot_wait)
        # self.get_objects_rel_pos(op_mode=sim.simx_opmode_oneshot_wait)

    def finish(self):
        sim.simxStopSimulation(self.client_id, sim.simx_opmode_oneshot_wait)

    def update(self):
        self.get_objects_rel_pos()
        self.get_objects_pos()

    def show_all_objects(self):
        self.base.show()
        self.J1.show()
        self.J3.show()
        self.J4.show()
        self.J5.show()
        self.J6.show()
        self.JL.show()
        self.JR.show()
        self.target.show()
        self.tip.show()
