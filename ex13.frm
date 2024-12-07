auto vector p;
auto index i;
local T1 = p1(i1)*p2(i2);
local T2 = p1(i1)*(p2(i2)+p3(i3));
local T3 = p1(i1)*p2(i1);
local T4 = p1(i1)*(p2(i2)+p3(i2));
local T5 = p1(i1)*(p2(i2)+p3(i1));
.sort
local T6 = p1(i1)*p2(i2)*p3(i1)*p4(i2);
local T7 = p1(i1)*p2(i1)*p3(i2)*p4(i2);
local T8 = p1(i1)*p2(i1)*p3(i1)*p4(i1);
local T9 = d_(i1,i2)*p1(i1)*p2(i2);
print;
.end

