`default_nettype none

module tt_um_down_counter (
    input  wire [7:0] ui_in,     // not used
    output wire [7:0] uo_out,    // counter output
    input  wire [7:0] uio_in,    // not used
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [7:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 8'd0;        // reset to 0
        else if (ena)
            count <= count - 1;   // DOWN counter
    end

    assign uo_out = count;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
