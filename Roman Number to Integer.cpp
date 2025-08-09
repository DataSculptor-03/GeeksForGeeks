

//User function template for C++

/*class Solution {
  public:
    int romanToDecimal(string &str) {
        // code here
    }
};*/


//User function template for C++

class Solution {
  public:
    int romanToDecimal(string &str)
    {
        // code here
        
        int count=0;
         int t=0;
            switch(str[str.length()-1])
            {
                case 'I':
                    count+=1;
                    t=1;
                    break;
                case 'V':
                    count+=5;
                    t=5;
                    break;
                case 'X':
                    count+=10;
                    t=10;
                    break;
                case 'L':
                    count+=50;
                    t=50;
                    break;
                case 'C':
                    count+=100;
                    t=100;
                    break;
                case 'D':
                    count+=500;
                    t=500;
                    break;
                case 'M':
                    count+=1000;
                    t=1000;
                    break;
            }
       
        for(int i=str.length()-2; i>=0; i--)
        {
            switch(str[i])
            {
                case 'I':
                if(t<=1)
                {    count+=1;
                    t=1;
                }
                else
                {
                    count-=1;
                }
                t=1;
                    break;
                case 'V':
                if(t<=5)
                    count+=5;
                else
                    count-=5;
                    t=5;
                    break;
                case 'X':
                if(t<=10)
                    count+=10;
                else
                    count-=10;
                    t=10;
                    break;
                case 'L':
                if(t<=50)
                    count+=50;
                else
                    count-=50;
                    t=50;
                    break;
                case 'C':
                if(t<=100)
                    count+=100;
                else
                    count-=100;
                    t=100;
                    break;
                case 'D':
                if(t<=500)
                    count+=500;
                else
                    count-=500;
                    t=500;
                    break;
                case 'M':
                if(t<=1000)
                    count+=1000;
                else
                    count-=1000;
                    t=1000;
                    break;
            }
        }
        return  count;
        
        
    }
};
