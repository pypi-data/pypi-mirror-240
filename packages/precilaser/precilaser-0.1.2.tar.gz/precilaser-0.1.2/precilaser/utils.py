import time

from rich.console import Console

from .amplifier import SHGAmplifier


def wait_until_shg_temperature_stable(
    amplifier: SHGAmplifier,
    temperature_setpoint: float,
    temp_stable: float = 0.02,
    time_stable: float = 10,
    timeout: float = 200,
    progress: bool = False,
) -> None:
    """
    Utility function to wait until the SHG temperature is stable to within temp_stable
    [C] for at least time_stable [s].

    Args:
        amplifier (SHGAmplifier): precilaser shg amplifier interface
        temperature_setpoint (float): temperature setpoint [C]
        temp_stable (float, optional): temperature stability range [C].
                                        Defaults to 0.02 C.
        time_stable (float, optional): time [s] to stay within temperature stability
                                        range. Defaults to 10 s.
        timeout (float, optional): timeout [s]. Defaults to 200 s.

    Raises:
        TimeoutError: raises a TimeoutError if the wait time exceeds timout
    """
    if progress:
        console = Console()
    else:

        class dummy:
            class status:
                def __init__(self, message: str):
                    pass

                def __enter__(self):
                    return None

                def __exit__(self, *exc):
                    return None

        console = dummy()  # type: ignore
    tstart = time.time()
    time_temp_stable = 0.0
    with console.status("Waiting for SHG crystal temperature to stabilize") as status:
        while True:
            temperature = amplifier.shg_temperature
            stable = abs(temperature - temperature_setpoint) < temp_stable
            if progress:
                if stable:
                    color = "green"
                else:
                    color = "red"
                status.update(
                    "Waiting for SHG crystal temperature to stabilize\n  set ="
                    f" {temperature_setpoint:.2f} C, act ="
                    f" [{color}]{temperature:.2f} C[/{color}]"
                )
            if stable:
                if time_temp_stable == 0.0:
                    time_temp_stable = time.time()
                elif time.time() - time_temp_stable > time_stable:
                    break
            else:
                time_temp_stable = 0
            if time.time() - tstart > timeout:
                raise TimeoutError(
                    "SHG crystal temperature stabilization wait time exceeded the"
                    f" preset limit of {timeout} seconds"
                )
            time.sleep(0.3)
