size = 0.003;
size_2 = 0.005;

L_x = 0.6; 
L_y = 0.24;
delta_clay = 0.02;
bottom_clay = 0.14;

//+ 4 angles of domain
Point(1) = {0, 0, 0, size};
Point(4) = {0, L_y, 0, size};
Point(5) = {L_x/2, 0, 0, size};
Point(6) = {L_x/2, L_y, 0, size};

//+ 2 points for the water enters
Point(9) = {L_x/4-0.02, L_y, 0, size};
Point(10) = {L_x/4+0.02, L_y, 0, size};
Point(11) = {L_x/4-0.015, L_y-0.02, 0, size};
Point(12) = {L_x/4+0.015, L_y-0.02, 0, size};

//+ 2 points sand 
Point(13) = {L_x/8*3-0.015, L_y/2, 0, size};
Point(14) = {L_x/8*3+0.015, L_y/2, 0, size};
//+
Line(1) = {1, 5};
//+
Line(2) = {5, 6};
//+
Line(3) = {6, 10};
//+
Line(4) = {10, 12};
//+
Line(5) = {12, 11};
//+
Line(6) = {11, 9};
//+
Line(7) = {9, 4};
//+
Line(8) = {4, 1};
//+
Line(9) = {13, 14};
//+
Line(10) = {14, 12};
//+
Line(11) = {11, 13};
//+
Curve Loop(1) = {7, 8, 1, 2, 3, 4, -10, -9, -11, 6};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {11, 9, 10, 5};
//+
Plane Surface(2) = {2};
//+
Physical Curve("zero flux", 10) = {7, 8, 1, 2, 3};
//+
Physical Curve("terrain interface", 1) = {11, 10, 9};
//+
Physical Curve("water table from 0", 41) = {6, 4, 5};
//+
Physical Surface("loam", 1) = {1};
//+
Physical Surface("sand", 2) = {2};
