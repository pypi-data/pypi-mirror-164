from biasgen import phantom3d, CoilSegments, \
                    view_coil_positioning, \
                    cage_constructor
from tests import IMG_FOLDER


def coil_setups():
    st_en_pnts = [[1,100],[2,25],[3,30]]

    c = CoilSegments(st_en_pnts)
    print('point paths:', c.get_point_paths())
    print('point pairs:', c.get_point_pairs())
    print('coord paths:', c.get_coord_paths(),'\n')

    print('point paths 0.5 zoom:', c.get_point_paths(0.5))
    print('point pairs 0.5 zoom:', c.get_point_pairs(0.5))
    print('coord paths 0.5 zoom:', c.get_coord_paths(0.5),'\n')

    c_line = CoilSegments(st_en_pnts, [(0,0,0), (1,0,0)])
    print('line point paths:', c_line.get_point_paths())
    print('line point pairs:', c_line.get_point_pairs())
    print('line coord paths:', c_line.get_coord_paths(),'\n')

    c_interp = CoilSegments(st_en_pnts, [(0,0,0), (1,0.5,0), (0.5,0,0.25)])
    print('interp point paths:', c_interp.get_point_paths())
    print('interp point pairs:', c_interp.get_point_pairs())
    print('interp coord paths:', c_interp.get_coord_paths(),'\n')


def view_cages():
    ph = phantom3d(64)

    coils = cage_constructor(2, (32,32,32), 32, 0.5, (25, 40))

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'coil2.png')

    coils = cage_constructor(3, (32,32,32), 32, 0.4, (40, 35), 0)

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'coil3.png')

    coils = cage_constructor(6, (32,32,32), 32, 0.6, (40, 35), 0)

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'coil6.png')

    coils = cage_constructor(13, (32,32,32), 32, 0, (40, 35), 0)

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'lines13.png')

    coils = cage_constructor([5,8], (32,32,32), 32, 0.6, (40, 35), 90, 180, (5,5))

    view_coil_positioning(ph, coils, full_save_path=IMG_FOLDER / 'phase58.png')


if __name__ == '__main__':
    coil_setups()
    view_cages()