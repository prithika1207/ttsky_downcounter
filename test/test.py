import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock


@cocotb.test()
async def test_downcounter(dut):
    dut._log.info("Starting Down Counter Test")

    # 🔥 ADD CLOCK (this was missing)
    clock = Clock(dut.clk, 10, unit="ns")  # 10ns period
    cocotb.start_soon(clock.start())

    # reset
    dut.ena.value = 1
    dut.rst_n.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1

    await Timer(20, unit="ns")

    prev = int(dut.uo_out.value)

    for i in range(10):
        await Timer(10, unit="ns")

        curr = int(dut.uo_out.value)
        dut._log.info(f"Cycle {i}: {curr}")

        if prev == 0:
            assert curr == 255, "Wrap error"
        else:
            assert curr == (prev - 1), f"Error: {prev} → {curr}"

        prev = curr
