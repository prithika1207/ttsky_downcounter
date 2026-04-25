import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_downcounter(dut):
    dut._log.info("Starting Down Counter Test")

    # Initialize
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Reset
    await Timer(50, unit="ns")
    dut.rst_n.value = 1
    await Timer(20, unit="ns")

    # Get initial value
    prev = int(dut.uo_out.value)

    # Check 10 cycles
    for i in range(10):
        await Timer(10, unit="ns")

        curr = int(dut.uo_out.value)
        dut._log.info(f"Cycle {i}: {curr}")

        # Check counting down
        if prev == 0:
            assert curr == 255, "Wrap error (0 → 255 failed)"
        else:
            assert curr == (prev - 1), f"Error: {prev} → {curr}"

        prev = curr


