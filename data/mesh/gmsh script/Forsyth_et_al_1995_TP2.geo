// Gmsh project created on Mon Aug 01 09:04:53 2022
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 6.5, 0, 1.0};
//+
Point(3) = {8, 0, 0, 1.0};
//+
Point(4) = {8, 6.5, 0, 1.0};
//+
Point(5) = {1, 4, 0, 1.0};
//+
Point(6) = {3, 4, 0, 1.0};
//+
Point(7) = {3, 5, 0, 1.0};
//+
Point(8) = {1, 5, 0, 1.0};
//+
Point(9) = {2.25, 6.5, 0, 1.0};
//+
Point(10) = {0, 6.1, 0, 1.0};
//+
Point(11) = {0, 5.6, 0, 1.0};
//+
Point(12) = {8, 5.6, 0, 1.0};
//+
Point(13) = {8, 6.1, 0, 1.0};
//+
Point(14) = {0, 5, 0, 1.0};
//+
Point(15) = {0, 4, 0, 1.0};
//+
Point(16) = {8, 5, 0, 1.0};
//+
Point(17) = {8, 4, 0, 1.0};


//+
Line(1) = {9, 2};
//+
Line(2) = {2, 10};
//+
Line(3) = {10, 11};
//+
Line(4) = {11, 14};
//+
Line(5) = {1, 3};
//+
Line(6) = {3, 17};
//+
Line(7) = {12, 13};
//+
Line(8) = {13, 4};
//+
Line(9) = {4, 9};
//+
Line(10) = {13, 10};
//+
Line(11) = {12, 11};
//+
Line(12) = {7, 8};
//+
Line(13) = {8, 5};
//+
Line(14) = {5, 6};
//+
Line(15) = {6, 7};
//+
Line(16) = {14, 8};
//+
Line(17) = {15, 5};
//+
Line(18) = {6, 17};
//+
Line(19) = {7, 16};
//+
Line(20) = {14, 15};
//+
Line(21) = {15, 1};
//+
Line(22) = {17, 16};
//+
Line(23) = {16, 12};



//+
Curve Loop(1) = {11, 4, 16, -12, 19, 23};
//+
Curve Loop(2) = {-16, 20, 17, -13};
//+
Curve Loop(3) = {21, 5, 6, -18, -14, -17};
//+
Curve Loop(4) = {22, -19, -15, 18};


//+ small rectangle
Curve Loop(5) = {12, 13, 14, 15};
//+ upper rectangle
Curve Loop(6) = {1, 2, -10, 8, 9};
//+ lower rectangle
Curve Loop(7) = {10, 3, -11, 7};

//+
Plane Surface(1) = {1};
//+
Plane Surface(5) = {2};
//+
Plane Surface(6) = {3};
//+
Plane Surface(7) = {4};
//+
Plane Surface(2) = {5};
//+
Plane Surface(3) = {6};
//+
Plane Surface(4) = {7};


//+
//Physical Curve("free drainage", 30) = {1};

//+
Physical Surface("zone 1", 1) = {3};
//+
Physical Surface("zone 2", 2) = {4};
//+
Physical Surface("zone 3", 3) = {1, 5, 6, 7};
//+
Physical Surface("zone 4", 4) = {2};


//+
Physical Curve("internal boundary", 1) = {10, 11, 16, 12, 19, 13, 15, 17, 14, 18};
//+
Physical Curve("No flow", 10) = {2, 3, 4, 10, 21, 5, 6, 22, 23, 7, 8, 9};
//+
Physical Curve("Flow", 11) = {1};

//+
Transfinite Curve {10, 11, 5} = 160 Using Bump 1;
//+
Transfinite Curve {9} = 114 Using Bump 1;
//+
Transfinite Curve {8, 2} = 8 Using Bump 1;
//+
Transfinite Curve {1} = 60 Using Bump 1;
//+
Transfinite Curve {3, 7} = 10 Using Bump 1;
//+
Transfinite Curve {4, 23} = 12 Using Bump 1;
//+
Transfinite Curve {20, 13, 15, 22, 16, 17} = 20 Using Bump 1;
//+
Transfinite Curve {12, 14} = 40 Using Bump 1;
//+
Transfinite Curve {19, 18} = 100 Using Bump 1;
//+
Transfinite Curve {21, 6} = 80 Using Bump 1;