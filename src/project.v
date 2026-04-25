`default_nettype none

module tt_um_downcounter (
    input  wire [7:0] ui_in,     // not used
    output wire [7:0] uo_out,    // counter output
    input  wire [7:0] uio_in,    // not used
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,       // enable
    input  wire       clk,       // clock
    input  wire       rst_n      // active low reset
);

    reg [7:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 8'd0;          // reset to 0
        else if (ena)
            count <= count - 1;     // count down
    end

    // output
    assign uo_out = count;

    // unused IOs
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // prevent unused warnings
    wire _unused = &{ui_in, uio_in};

endmodule
