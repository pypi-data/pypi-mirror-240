import os
import time

import numpy as np
import pore_mapper as pm


def run_calculation(prefix, pore_volume):
    # Read in host from xyz file.
    host = pm.Host.init_from_xyz_file(path=f"{prefix}.xyz")
    host = host.with_centroid([0.0, 0.0, 0.0])

    # Define calculator object.
    calculator = pm.Inflater(bead_sigma=1.2, centroid=host.get_centroid())

    # Run calculator on host object, analysing output.
    print(f"doing {prefix}")
    stime = time.time()
    final_result = calculator.get_inflated_blob(host=host)
    print(f"run time: {time.time() - stime}")
    pore = final_result.pore
    blob = final_result.pore.get_blob()
    windows = pore.get_windows()
    print(final_result)
    print(
        f"step: {final_result.step}\n"
        f"num_movable_beads: {final_result.num_movable_beads}\n"
        f"windows: {windows}\n"
        f"blob: {blob}\n"
        f"pore: {pore}\n"
        f"blob_max_diam: {blob.get_maximum_diameter()}\n"
        f"pore_max_rad: {pore.get_maximum_distance_to_com()}\n"
        f"pore_mean_rad: {pore.get_mean_distance_to_com()}\n"
        f"pore_volume: {pore.get_volume()}\n"
        f"num_windows: {len(windows)}\n"
        f"max_window_size: {max(windows)}\n"
        f"min_window_size: {min(windows)}\n"
        f"asphericity: {pore.get_asphericity()}\n"
        f"shape anisotropy: {pore.get_relative_shape_anisotropy()}\n"
    )
    print()

    # Do final structure.
    host.write_xyz_file(f"example_output/{prefix}_final.xyz")
    blob.write_xyz_file(f"example_output/{prefix}_blob_final.xyz")
    pore.write_xyz_file(f"example_output/{prefix}_pore_final.xyz")

    # A quick check for no changes.
    print(pore.get_volume(), pore_volume)
    assert np.isclose(pore.get_volume(), pore_volume, atol=1e-6, rtol=0)


def main():
    if not os.path.exists("example_output"):
        os.mkdir("example_output")

    names = (
        ("cc3", 200.0827435501178),
        ("moc2", 727.9224999790649),
        ("moc1", 9.142119630617236),
        ("hogrih_cage", 536.9120376447318),
        ("hogsoo_cage", 1452.5658535480663),
        ("hogsii_cage", 292.31476121263916),
        ("yamashina_cage_", 1674.5016354156583),
    )

    for prefix, pore_volume in names:
        run_calculation(prefix, pore_volume)


if __name__ == "__main__":
    main()
