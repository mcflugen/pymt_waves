


cdef extern from "waves/bmi_waves.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_waves(BMI_Model *model)


