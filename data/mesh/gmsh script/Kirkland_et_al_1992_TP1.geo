size = 1.0;

//bottom row
Point(1) = {0, 0, 0, size};
Point(2) = {1.50, 0, 0, size};
Point(3) = {3.50, 0, 0, size};
Point(4) = {5.00, 0, 0, size};

//mid-bottom row
Point(5) = {0, 1.00, 0, size};
Point(6) = {1.50, 1.00, 0, size};
Point(7) = {3.50, 1.00, 0, size};
Point(8) = {5.00, 1.00, 0, size};

//mid-top row
Point(9) = {0, 2.00, 0, size};
Point(10) = {1.50, 2.00, 0, size};
Point(11) = {3.50, 2.00, 0, size};
Point(12) = {5.00, 2.00, 0, size};

//top row
Point(13) = {0, 3.00, 0, size};
Point(14) = {1.50, 3.00, 0, size};
Point(15) = {3.50, 3.00, 0, size};
Point(16) = {5.00, 3.00, 0, size};

//2 points for q
Point(17) = {2.00, 3.00, 0, size};
Point(18) = {3.00, 3.00, 0, size};

//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 8};
//+
Line(5) = {8, 12};
//+
Line(6) = {12, 16};
//+
Line(7) = {16, 15};
//+
Line(8) = {15, 18};
//+
Line(9) = {18, 17};
//+
Line(10) = {17, 14};
//+
Line(11) = {14, 13};
//+
Line(12) = {13, 9};
//+
Line(13) = {9, 5};
//+
Line(14) = {5, 1};
//+
Line(15) = {14, 10};
//+
Line(16) = {10, 6};
//+
Line(17) = {6, 2};
//+
Line(18) = {15, 11};
//+
Line(19) = {11, 7};
//+
Line(20) = {7, 3};
//+
Line(21) = {9, 10};
//+
Line(22) = {10, 11};
//+
Line(23) = {11, 12};
//+
Line(24) = {5, 6};
//+
Line(25) = {6, 7};
//+
Line(26) = {7, 8};
//+
Curve Loop(1) = {1, -17, -24, 14};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {2, -20, -25, 17};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {3, 4, -26, 20};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {13, 24, -16, -21};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {-22, -19, 25, 16};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {-23, 5, 26, 19};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {6, 7, 18, 23};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {9, 10, 15, 22, -18, 8};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {11, 12, 21, -15};
//+
Plane Surface(9) = {9};
//+
Physical Surface("sand", 1) = {8, 4, 6, 2};
//+
Physical Surface("clay", 2) = {9, 7, 5, 1, 3};
//+
Physical Curve("zero flux", 10) = {10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8};
//+
Physical Curve("constant flux not zero", 11) = {9};
//+
Physical Curve("interface clay sand", 1) = {15, 21, 16, 24, 25, 22, 18, 23, 19, 26, 20, 17};


//+
Transfinite Curve {1, 2, 3, 24, 25, 26, 21, 22, 23, 11, 7} = 60 Using Bump 1;
//+
Transfinite Curve {10, 8} = 20 Using Bump 1;
//+
Transfinite Curve {9} = 40 Using Bump 1;
//+
Transfinite Curve {14, 17, 20, 4, 13, 16, 19, 5, 12, 15, 18, 6} = 40 Using Bump 1;
