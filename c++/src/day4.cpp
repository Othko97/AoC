#include <iostream>   //cout
#include <sstream>    //stringstream
#include <fstream>    //ifstream
#include <vector>     //vector
#include <string>     //string
#include <algorithm>  //sort

//Prototyping
bool valid(std::string s);
int countvalid(std::vector<std::string> list);
bool anagramvalid(std::string s);
int countanagramvalid(std::vector<std::string> list);

int main()
{
  std::vector<std::string> list;
  std::ifstream data ("../data/day4.txt");
  std::string s;
  
  if (data.is_open())
  {
    while (getline(data, s))
    {
      list.push_back(s);
    }
  }
  std::cout << countvalid(list) << std::endl;
  std::cout << countanagramvalid(list) << std::endl;
  return 0;
}

bool valid(std::string s)
{
  std::vector<std::string> old;
  std::stringstream stream(s);
  for (std::string s; stream >> s;)
  {
    for (std::string t : old)
    {
      if (t == s)
      {
        return false;
      }
    }
    old.push_back(s);
  }
  return true;
}

int countvalid(std::vector<std::string> list)
{
  int sum = 0;
  for (std::string s : list)
  {
    if (valid(s))
    {
      sum++;
    }
  }
  return sum;
}

bool anagramvalid(std::string s)
{
  std::vector<std::string> old;
  std::stringstream stream(s);
  for (std::string s; stream >> s;)
  {
    std::sort(s.begin(), s.end());
    for (std::string t : old)
    {
      if (t == s)
      {
        return false;
      }
    }
    old.push_back(s);
  }
  return true;
}

int countanagramvalid(std::vector<std::string> list)
{
  int sum = 0;
  for (std::string s : list)
  {
    if (anagramvalid(s))
    {
      sum++;
    }
  }
  return sum;
}