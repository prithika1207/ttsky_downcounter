import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_down_counter(dut):
    dut._log.info("Starting Down Counter Test")

    # reset
    dut.ena.value = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1

    await Timer(20, unit="ns")

    # capture first value
    prev = int(dut.uo_out.value)

    # check that it is counting DOWN
    for i in range(10):

        await Timer(10, unit="ns")
        curr = int(dut.uo_out.value)

        dut._log.info(f"Cycle {i}: {curr}")

        # check it decreases (wrap allowed)
        # allow wrap from 0 -> 255
        if prev == 0:
            assert curr == 255, "Wrap error"
        else:
            assert curr == (prev - 1), f"Counter error: {prev} → {curr}"

        prev = curr
