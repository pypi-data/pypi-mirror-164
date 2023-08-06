import biasgen
from biasgen import phantom3d, SensitivitySettings, \
                    cage_constructor, view_center_axes, \
                    compute_field, field_readout, compute_sensitivity, \
                    bias_sum_of_squares, view_coil_positioning
from tests import IMG_FOLDER

import numpy as np


def mag_tests():
    ph = phantom3d()
    coils = cage_constructor(2, (64,64,64), 64, 0.5, (50, 80))
    uv = SensitivitySettings(1,1).uv
    tl_names = ['Z-axis', 'Y-axis', 'X-axis']
    ph_mask = ph > 0

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'coils2_128.png')

    field = compute_field(coils, ph.shape, sum_coils=True, scale_fctr=0.5)

    field_meas = field_readout(field, uv)

    view_center_axes(np.abs(field_meas), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2field_sum.png')

    view_center_axes(field_meas, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2field_sum_cmplx.png')

    field_coll = compute_field(coils, ph.shape, scale_fctr=0.5)
    field_meas_coll = field_readout(field_coll, uv)

    view_center_axes(np.abs(field_meas_coll), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2field_coll.png')

    view_center_axes(field_meas_coll, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2field_coll_cmplx.png')

    field_ncoll = compute_field(coils, ph.shape, scale_fctr=0.5, collect_within_coil=False)
    field_meas_ncoll = field_readout(field_ncoll, uv)

    view_center_axes(np.abs(field_meas_ncoll), ph_mask,
                     full_save_path=IMG_FOLDER / '2field_ncoll.png')

    view_center_axes(field_meas_ncoll, ph_mask, 
                     full_save_path=IMG_FOLDER / '2field_ncoll_cmplx.png')

    lines = cage_constructor(4, (64,64,64), 64, 0, (70, 60))
    view_coil_positioning(ph, lines, full_save_path=IMG_FOLDER / 'lines4ln.png')

    field_coll = compute_field(lines, ph.shape, scale_fctr=0.5)
    field_meas_coll = field_readout(field_coll, uv)


    view_center_axes(np.abs(field_meas_coll), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4lnfield_coll.png')

    view_center_axes(field_meas_coll, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4lnfield_coll_cmplx.png')


def sens_tests():
    ph = phantom3d()
    coils = cage_constructor(2, (64,64,64), 64, 0.5, (50, 80))
    sens_settings = SensitivitySettings(5,1)
    tl_names = ['Z-axis', 'Y-axis', 'X-axis']
    ph_mask = ph > 0

    sens = compute_sensitivity(coils, sens_settings, ph.shape, batch_sz=1,
                               scale_fctr=0.5)
    bias = bias_sum_of_squares(sens)

    view_center_axes(np.abs(sens), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2sens.png')

    view_center_axes(sens, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2sens_cmplx.png')

    view_center_axes(bias, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '2bias.png')
    
    lines = cage_constructor(4, (64,64,64), 64, 0, (70, 60))

    sens = compute_sensitivity(lines, sens_settings, ph.shape, batch_sz=1,
                               scale_fctr=0.5, collect_within_coil=False)
    bias = bias_sum_of_squares(sens)

    view_center_axes(np.abs(sens), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4sens.png')

    view_center_axes(sens, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4sens_cmplx.png')

    view_center_axes(bias, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4bias.png')

def sens_patterns3():
    ph = phantom3d(256)
    coils = cage_constructor(3, (128,128,128), 128, 0.5, (150, 115), 0)
    sens_settings = SensitivitySettings((7,7,7), (0.5,1.75,1.75), (0,-0.25,-0.25))
    tl_names = ['Z-axis', 'Y-axis', 'X-axis']
    ph_mask = ph > 0

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'lines3_256.png')

    field = compute_field(coils, ph.shape, batch_sz=1, scale_fctr=0.125)

    field_meas = field_readout(field, sens_settings.uv)

    view_center_axes(np.abs(field_meas), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '3mag.png')

    view_center_axes(field_meas, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '3mag_cmplx.png')

    sens = compute_sensitivity(coils, sens_settings, ph.shape, batch_sz=1,
                               scale_fctr=0.125)
    bias = bias_sum_of_squares(sens)

    view_center_axes(np.abs(sens), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '3sens.png')

    view_center_axes(sens, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '3sens_cmplx.png')

    view_center_axes(bias*ph, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '3bias.png')


def sens_patterns4():
    ph = phantom3d(256)
    coils = cage_constructor(4, (128,128,128), 128, 0.5, (150, 115), 0)
    sens_settings = SensitivitySettings((11,11,11), (1.5,1.5,1.75), (0,-0.75,0))
    tl_names = ['Z-axis', 'Y-axis', 'X-axis'] 
    ph_mask = ph > 0

    #view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'lines4_256.png')

    #field = compute_field(coils, ph.shape, batch_sz=1, scale_fctr=0.25)

    #field_meas = field_readout(field, sens_settings.uv)

    #view_center_axes(np.abs(field_meas), ph_mask, title_names=tl_names, 
    #                 full_save_path=IMG_FOLDER / '4mag.png')

    #view_center_axes(field_meas, ph_mask, title_names=tl_names, 
    #                 full_save_path=IMG_FOLDER / '4mag_cmplx.png')

    sens = compute_sensitivity(coils, sens_settings, ph.shape, batch_sz=1,
                               scale_fctr=0.125)
    bias = bias_sum_of_squares(sens)

    view_center_axes(np.abs(sens), ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4sens.png')

    view_center_axes(sens, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4sens_cmplx.png')

    view_center_axes(bias, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4bias.png')
   
    view_center_axes(bias*ph, ph_mask, title_names=tl_names, 
                     full_save_path=IMG_FOLDER / '4bias_ph.png')


def sens_phase():
    ph = phantom3d(256)
    ph_mask = ph > 0

    sens_settings = SensitivitySettings((7,7,7), (0.5,1.75,1.75), (0,-0.25,-0.25))
    coils = cage_constructor([5,8], (128,128,128), 128, 0.6, (160, 125), 90, 180, (20,20))

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'phase58.png')

    field = compute_field(coils, ph.shape, batch_sz=2, scale_fctr=0.125)

    field_meas = field_readout(field, sens_settings.uv)

    view_center_axes(np.abs(field_meas), ph_mask, 
                     full_save_path=IMG_FOLDER / 'phasemag.png')

    view_center_axes(field_meas, ph_mask, 
                     full_save_path=IMG_FOLDER / 'phasemag_cmplx.png')

    sens = compute_sensitivity(coils, sens_settings, ph.shape, batch_sz=2,
                               scale_fctr=0.125)
    bias = bias_sum_of_squares(sens)

    view_center_axes(np.abs(sens), ph_mask, 
                     full_save_path=IMG_FOLDER / 'phasesens.png')

    view_center_axes(sens, ph_mask,
                     full_save_path=IMG_FOLDER / 'phasesens_cmplx.png')

    view_center_axes(bias*ph, ph_mask,
                     full_save_path=IMG_FOLDER / 'phasebias.png')


if __name__ == '__main__':
    biasgen.use_gpu(True)
    #mag_tests()
    #sens_tests()
    sens_patterns4()
