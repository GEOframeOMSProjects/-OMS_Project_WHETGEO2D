size = 1.0;

Point(1) = {0, 0, 0, size};
Point(2) = {5.00, 0, 0, size};
Point(3) = {5.00, 3.00, 0, size};
Point(4) = {0, 3.00, 0, size};
Point(5) = {0, 1.00, 0, size};
Point(6) = {5.00, 1.00, 0, size};
Point(7) = {1.00, 2.00, 0, size};
Point(8) = {4.00, 2.00, 0, size};

//2 points for q
Point(9) = {1.00, 3.00, 0, size};
Point(10) = {4.00, 3.00, 0, size};

Point(11) = {0, 2.00, 0, size};
Point(12) = {5.00, 2.00, 0, size};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 6};
//+
Line(3) = {6, 12};
//+
Line(4) = {12, 3};
//+
Line(5) = {3, 10};
//+
Line(6) = {10, 9};
//+
Line(7) = {9, 4};
//+
Line(8) = {4, 11};
//+
Line(9) = {11, 5};
//+
Line(10) = {5, 1};
//+
Line(11) = {5, 6};
//+
Line(12) = {11, 7};
//+
Line(13) = {7, 9};
//+
Line(14) = {7, 8};
//+
Line(15) = {8, 10};
//+
Line(16) = {8, 12};
//+
Curve Loop(1) = {10, 1, 2, -11};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {-12, -14, -16, 3, 11, 9};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {8, 12, 13, 7};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {6, -13, 14, 15};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {5, -15, 16, 4};
//+
Plane Surface(5) = {5};

//+
Physical Surface("sand", 1) = {4, 1};
//+
Physical Surface("clay", 2) = {3, 2, 5};

//+
Physical Curve("zero flux", 10) = {7, 8, 9, 10, 1, 2, 3, 4, 5};
//+
Physical Curve("constant flux not zero", 11) = {6};
//+
Physical Curve("interface clay sand", 1) = {13, 12, 14, 15, 16, 11};


//+
Transfinite Curve {1, 11} = 100 Using Bump 1;
//+
Transfinite Curve {10, 2, 9, 3, 8, 13, 15, 4, 7, 12, 16, 5} = 20 Using Bump 1;
//+
Transfinite Curve {6, 14} = 60 Using Bump 1;
