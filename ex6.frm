on highfirst;
symbol a,b,c;
local T1 = (a+b+c)^2;
.sort
local T2 = (a+b+c)*T1;
.sort
id c = -(a+3*b)/2;
print;
.end

