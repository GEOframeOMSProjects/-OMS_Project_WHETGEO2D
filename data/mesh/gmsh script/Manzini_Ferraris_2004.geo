L_x = 1;
L_z = 1;
size = 1/50;


For i In {0:100}
	Point(i+1) = {i/100, (0.1*(1-Cos(Pi*i/100/L_x))+0.45)*L_z, 0, size};
	tags_for_spline[i] = i+1;
EndFor//+

Spline(1) = {tags_for_spline[]};

//+
Point(102) = {0, 0, 0, size};
//+
Point(103) = {L_x, 0, 0, size};
//+
Point(104) = {L_x, L_z, 0, size};
//+
Point(105) = {0, L_z, 0, size};
//+
Line(2) = {102, 103};
//+
Line(3) = {105, 104};
//+
Line(4) = {105, 1};
//+
Line(5) = {1, 102};
//+
Line(6) = {103, 101};
//+
Line(7) = {101, 104};
//+
Curve Loop(1) = {1, 7, -3, 4};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {1, -6, -2, -5};
//+
Plane Surface(2) = {2};
//+
Physical Surface("top layer", 1) = {1};
//+
Physical Surface("bottom layer", 2) = {2};
//+
Physical Curve("top and bottom Dirichlet", 21) = {3, 2};
//+
Physical Curve("left and right Neumann", 11) = {4, 5, 6, 7};
//+
Physical Curve("interface", 1) = {1};
