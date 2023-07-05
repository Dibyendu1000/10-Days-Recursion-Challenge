#include <bits/stdc++.h>

int atoiHelper(string str, int i, int ans)
{
    if(i == str.size())
    {
        return ans;
    }

    if('0' <= str[i] && str[i] <= '9')
    {
        ans = (ans*10)+(str[i]-'0');
    }
    
    return atoiHelper(str, i+1, ans);

}
int atoi(string str) {
    // Write your code here.
    int ans = atoiHelper(str, 0, 0);
    return str[0] == '-'? 0-ans:ans;
}