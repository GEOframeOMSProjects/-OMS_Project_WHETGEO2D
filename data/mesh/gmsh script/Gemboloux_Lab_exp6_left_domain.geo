size = 0.003;
size_2 = 0.00001;

L_x = 0.6; 
L_y = 0.24;
delta_clay = 0.02;
bottom_clay = 0.14;

//+ 4 angles of domain
Point(1) = {0, 0, 0, size};
Point(2) = {0, L_y, 0, size};
Point(3) = {L_x/2, 0, 0, size};
Point(4) = {L_x/2, L_y, 0, size};

//+ 2 points for the water enters
Point(5) = {L_x/4-0.02, L_y, 0, size};
Point(6) = {L_x/4+0.02, L_y, 0, size};
Point(7) = {L_x/4, L_y-0.02, 0, size};

//+ 4 points sand 
Point(8) = {L_x/4-0.015, L_y/4*3, 0, size};
Point(9) = {L_x/4+0.015, L_y/4*3, 0, size};
Point(10) = {L_x/8-0.015, L_y/4, 0, size};
Point(11) = {L_x/8+0.015, L_y/4, 0, size};

//+
Line(1) = {1, 3};
//+
Line(2) = {3, 4};
//+
Line(3) = {4, 6};
//+
Line(4) = {6, 7};
//+
Line(5) = {7, 5};
//+
Line(6) = {5, 2};
//+
Line(7) = {2, 1};
//+
Line(8) = {10, 11};
//+
Line(9) = {11, 9};
//+
Line(10) = {9, 8};
//+
Line(11) = {8, 10};
//+
Curve Loop(1) = {6, 7, 1, 2, 3, 4, 5};
//+
Curve Loop(2) = {11, 8, 9, 10};
//+
Plane Surface(1) = {1, 2};
//+
Plane Surface(2) = {2};
//+
Physical Curve("zero flux", 10) = {6, 7, 1, 2, 3};
//+
Physical Curve("terrain interface", 1) = {8, 9, 11, 10};
//+
Physical Curve("water column from 0", 41) = {5, 4};
//+
Physical Surface("loam", 1) = {1};
//+
Physical Surface("sand", 2) = {2};
