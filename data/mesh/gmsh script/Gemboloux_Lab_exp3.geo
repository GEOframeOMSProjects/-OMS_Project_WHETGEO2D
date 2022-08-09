size = 0.03;
size_2 = 0.005;

L_x = 0.6; 
L_y = 0.24;
delta_clay = 0.02;
bottom_clay = 0.14;

//+ 4 angles of domain
Point(1) = {0, 0, 0, size};
Point(2) = {L_x, 0, 0, size};
Point(3) = {L_x, L_y, 0, size};
Point(4) = {0, L_y, 0, size};

//+ 4 angles of clay layer
Point(5) = {0, bottom_clay, 0, size};
Point(6) = {L_x, bottom_clay, 0, size};
Point(7) = {L_x, bottom_clay+delta_clay, 0, size};
Point(8) = {0, bottom_clay+delta_clay, 0, size};

//+ 2 points that define the segment which through the water enters
Point(9) = {L_x/2-0.02, L_y, 0, size};
Point(10) = {L_x/2+0.02, L_y, 0, size};
Point(11) = {L_x/2, L_y-0.02, 0, size};

//+
Line(1) = {1, 2};
//+
Line(2) = {2, 6};
//+
Line(3) = {6, 7};
//+
Line(4) = {7, 3};
//+
Line(5) = {3, 10};
//+
Line(6) = {10, 11};
//+
Line(7) = {11, 9};
//+
Line(8) = {9, 4};
//+
Line(9) = {4, 8};
//+
Line(10) = {8, 5};
//+
Line(11) = {5, 1};
//+
Line(12) = {5, 6};
//+
Line(13) = {7, 8};
//+
Curve Loop(1) = {8, 9, -13, 4, 5, 6, 7};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {13, 10, 12, 3};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {1, 2, -12, 11};
//+
Plane Surface(3) = {3};
//+
Physical Curve("zero flux", 10) = {8, 9, 10, 11, 1, 2, 3, 4, 5};
//+
Physical Curve("interface terrains", 1) = {13, 12};
//+
Physical Curve("water column from 0", 41) = {7, 6};

//+
Physical Surface("loam", 1) = {1, 3};

//+
Physical Surface("sand",2) = {2};
