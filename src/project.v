`default_nettype none

module tt_um_downcounter (
    input  wire [7:0] ui_in,     // unused
    output wire [7:0] uo_out,    // counter output
    input  wire [7:0] uio_in,    // unused
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [7:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 8'd0;        // reset
        else if (ena)
            count <= count - 1;   // down counter
    end

    assign uo_out = count;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

endmodule
