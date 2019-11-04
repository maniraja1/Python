class flatten_dict:

    def __new__(self,input_dict,*,sep='_'):
        self.input_dict = input_dict
        self.sep=sep
        self.output_dict={}
        self.flatten(self, self.input_dict,self.sep)
        return self.output_dict

    def flatten(self, inp,sep,parentkey=''):
        # print(f"Input:{inp}")
        for k,v in inp.items():
            if type(v) is dict:
                if parentkey == '':
                    parentkey2 = k
                else:
                    parentkey2 = parentkey+sep+k
                    parentkey=''
                # print(f"parentkey:{parentkey}")
                # print(f"v:{v}")
                self.flatten(self,v,sep,parentkey2)
            else:
                if parentkey == '':
                    self.output_dict[k] = v
                else:
                    self.output_dict[parentkey+sep+k] = v


x = flatten_dict({'vowels': {'a': 1, 'e': 4}, 'consonants': {'z': 2, 'v': 3}},sep='_')
print(x)
print(flatten_dict({'vowels': {'a': 1, 'e': 2}, 'b': 4}))

stuff = {'red': {'fruit': {'apple': 4}}, 'green': {'fruit': {'grape': 8}}}
print(flatten_dict(stuff, sep='/'))

