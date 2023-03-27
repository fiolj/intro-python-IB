class Test{
     private:
        int n;
     public:
        Test(int k){
            n=k;
        }
        void setInt(int k){
            n = k;
        }
        int getInt(){
            return n;
        }
};

extern "C" 
{
    // include below each method you want to make visible outside
    Test* init(int k) {return new Test(k);}
    void setInt(Test *self, int k) {self->setInt(k);}
    int getInt(Test *self) {return self->getInt();}
    
    // Add the declaration '__declspec(dllexport)' before each function in Windows
}