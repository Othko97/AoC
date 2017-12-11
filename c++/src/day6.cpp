#include <iostream>   //cout
#include <vector>     //vector
#include <climits>    //INT_MIN
#include <fstream>    //ifstream
#include <sstream>    //stringstream
#include <string>     //string

int getmaxpos(int array[16]);
void reallocate(int array[16]);
int getloop(int array[16]);
int getlooplength(int array[16]);
std::string tostring(int array[16]);
bool in(std::vector<std::string> states, std::string str);
int inpos(std::vector<std::string> states, std::string str);

int main()
{
  int array[16];
  std::ifstream data ("../data/day6.txt");
  std::string s;
  if (data.is_open())
  {
    getline(data, s);
    std::stringstream stream(s);
    for (int i = 0; i < 16; i++)
    {
      int x = 0;
      stream >> x;
      array[i] = x;
    }
  }
  std::cout << getloop(array) << std::endl;
  std::cout << getlooplength(array) << std::endl;
  return 0;
}

int getmaxpos(int array[16])
{
  int max = 0;
  for (int i = 0; i < 16; i++)
  {
    if (array[i] > array[max])
    {
      max = i;
    }
  }
  return max;
}

void reallocate(int array[16])
{
  int maxpos = getmaxpos(array), noblocks = array[maxpos];
  array[maxpos] = 0;
  for (int i = 1; i <= noblocks; i++)
  {
    array[(maxpos + i) % 16] += 1;
  }
}

int getloop(int array[16])
{
  int temp[16];
  for (int i = 0; i < 16; i++)
  {
    temp[i] = array[i];
  }
  int n = 1;
  reallocate(temp);
  std::string tempstring = tostring(temp);
  std::vector<std::string> prevstates;
  prevstates.push_back(tostring(array));
  while (!(in(prevstates, tempstring)))
  {
    prevstates.push_back(tempstring);
    reallocate(temp);
    n += 1;
    tempstring = tostring(temp);
  }
  return n;
}

int getlooplength(int array[16])
{
  int temp[16];
  for (int i = 0; i < 16; i++)
  {
    temp[i] = array[i];
  }
  int n = 1;
  reallocate(temp);
  std::string tempstring = tostring(temp);
  std::vector<std::string> prevstates;
  prevstates.push_back(tostring(array));
  while (!(inpos(prevstates, tempstring)))
  {
    prevstates.push_back(tempstring);
    reallocate(temp);
    n += 1;
    tempstring = tostring(temp);
  }
  int pos = inpos(prevstates, tempstring) - 1;
  return prevstates.size() - pos;
}

std::string tostring(int array[16])
{
  std::string strarray = "";
  for (int i = 0; i < 16; i++)
  {
    strarray += (char)('0' + array[i]);
    strarray += ',';
  }
  return strarray;
}

bool in(std::vector<std::string> states, std::string str)
{
  for (std::string s : states)
  {
    if (s == str)
    {
      return true;
    }
  }
  return false;
}

int inpos(std::vector<std::string> states, std::string str)
{
  for (int i = 0; i < states.size(); i++)
  {
    if (states[i] == str)
    {
      return i + 1;
    }
  }
  return 0;
}