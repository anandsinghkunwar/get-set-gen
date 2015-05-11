def to_camel_case(snake_str):
	components = snake_str.split('_')
	return components[0] + "".join(x.title() for x in components[1:])
n=input("Enter number of columns that need getter setter method?\n")
s=""
getter=""
setter=""
a=''
for i in xrange(n):
	c=raw_input("Enter variable name?(in snake case)\n")
	getter="get_" + str(c);
	setter="set_"+c;
	getter=to_camel_case(getter)
	setter=to_camel_case(setter)
	
	s=s+ "public function "+setter+"($"+c+") {"+"\n"
	s=s+ "    $this->"+c+"="+"$"+c+";"+"\n"
	s=s+ "}"+"\n"
	s=s+ "public function "+getter+"() {"+"\n"
     	s=s+ "    return $this->"+c+";"+"\n"
      	s=s+ "}"+"\n"
print s
