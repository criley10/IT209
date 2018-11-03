#---------------------------------------------------------------------
# IT209_093.py   - demonstrates the multiple inheritance diamond problem
#                 Uses super() to call parent class method.
#
# Gene Shuman      10/15/2018 (originally created 03/05/2018) 
#---------------------------------------------------------------------

class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print('Calling method on Base Class')
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print('Calling method on Left SubClass')
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print('Calling method on Right SubClass')
        self.num_right_calls += 1

class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me( )
        print('Calling method on Left SubClass')
        self.num_sub_calls += 1

   
s = SubClass( )
s.call_me( )
print('# SubClass calls:      ', s.num_sub_calls)
print('# LeftSubClass calls:  ', s.num_left_calls)
print('# RightSubClass calls: ', s.num_right_calls)      
print('# BaseClass calls:     ', s.num_base_calls)
