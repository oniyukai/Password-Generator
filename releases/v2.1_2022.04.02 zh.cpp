#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
string convertToString(char* a)
{
    string s = a;
    return s;
}
int main()
{
    cout << "--------------------" << endl << "密碼生成器 Version 2.1_2022.04.02" << endl << "Made by YU KAI" << endl << "--------------------" << endl << endl;
    for (int k=0; k<99; k++)
    {
        int n;
        cout << "輸入密碼的長度:";
        cin >> n;
        srand(time(0));
        int groups;
        cout << "輸入生成幾組密碼:";
        cin >> groups;
        string alphanum("");
        string announcement[]={"是否要加入1-9？ [Y/N] ","是否要加入a-z？ [Y/N] ","是否要加入A-Z？ [Y/N] ","是否要加入「!@#$\%^&*」？ [Y/N] "};
        string character[]={"0123456789","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","!@#$\%^&*"};
		string answer;
        for(int j=0;j<4;j++)
        {
            cout << announcement[j];
            cin >> answer;
            if (answer == convertToString("Y") or answer == convertToString("y"))
                alphanum += character[j];
        }
        cout << "是否要輸入而外字符？ [Y/N] " ;
        cin >> answer;
        if (answer == convertToString("Y") or answer == convertToString("y"))
        {
            string add;
            cout << "輸入而外字符:" << endl;
            cin >> add;
            alphanum += add;
        }
        int string_length = alphanum.length() -1;
        cout << "生成的密碼:" << endl;
        for (groups; groups>0; groups--)
        {
            for (int i = 0; i < n; i++)
                cout << alphanum[rand() % string_length];
            cout << endl;
        }
        cout << endl;
    }
    cout << "偵測到錯誤：這可能是產生過多次密碼或者是在第一或第二題輸入錯誤的回答";
    return 0;
}