dim 3;
auto vector p;
auto index i;
local T1 = e_(i1,i2,i3)*p1(i1);
local T2 = e_(i1,i2,i3)*p1(i1)*p2(i2);
local T3 = e_(i1,i2,i3)*p1(i1)*p2(i2)*p3(i3);
.sort
local T4 = e_(i1,i2,i3)*e_(i4,i5,i6);
local T5 = e_(i1,i2,i3)*e_(i3,i5,i6);
local T6 = e_(i1,i2,i3)*e_(i2,i5,i6);
local T7 = e_(i1,i2,i3)*e_(i2,i3,i6);
local T8 = e_(i1,i2,i3)*e_(i1,i2,i3);
local T9 = e_(i1,i2,i3)*p1(i1)*p2(i2)*p1(i3);
local T10 = e_(i1,i2,i3)*d_(i1,i2);
local T10 = e_(i1,i2,i3)*d_(i1,i4);
print;
.end

