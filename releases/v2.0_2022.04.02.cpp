#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
int main()
{
    cout << "--------------------" << endl << "Password Generator  Version 2.0_2022.04.02" << endl << "Made by YU KAI" << endl << "--------------------" << endl << endl;
    while(true)
    {
        int n;
        cout << "Enter the length of the password:";
        cin >> n;
        srand(time(0));
        int groups;
        cout << "Enter several sets of generated passwords:";
        cin >> groups;
        string alphanum("");
        string announcement[]={"Whether to add 1-9? [Y/N] ","Whether to add a-z? [Y/N] ","Whether to add A-Z? [Y/N] ","Whether to add \"!@#$\%^&*\"? [Y/N] "};
        string character[]={"0123456789","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","!@#$\%^&*"};
        char answer;
        for(int j=0;j<4;j++)
        {
            cout << announcement[j];
            cin >> answer;
            if (answer == 'Y' or answer == 'y')
                alphanum += character[j];
        }
        cout << "Whether to enter characters outside? [Y/N] ";
        cin >> answer;
        if (answer == 'Y' or answer == 'y')
        {
            string add;
            cout << "Enter the outer characters:" << endl;
            cin >> add;
            alphanum += add;
        }
        int string_length = alphanum.length() -1;
        cout << "Generated password:" << endl;
        for (groups; groups>0; groups--)
        {
            for (int i = 0; i < n; i++)
                cout << alphanum[rand() % string_length];
            cout << endl;
        }
        cout << endl;
    }
    return 0;
}