#include <iostream> //cout
#include <vector>   //vector
#include <fstream>  //ifstream
#include <string>   //string
#include <sstream>  //stringstream

int getsteps(std::vector<int> list);
int getsteps2(std::vector<int> list);

int main()
{
  std::vector<int> list;  
  std::ifstream data ("../data/day5.txt");
  std::string s;
  if (data.is_open())
  {
    while (getline(data, s))
    {
      std::stringstream stream(s);
      int x = 0;
      stream >> x;
      list.push_back(x);
    }
  }
  std::cout << getsteps(list) << std::endl;
  std::cout << getsteps2(list) << std::endl;
  return 0;
}

int getsteps(std::vector<int> list)
{
  int pos = 0, steps = 0, prev;
  while (pos < list.size())
  {
    prev = pos;
    pos = pos + list.at(pos);
    list.at(prev) += 1;
    steps += 1;
  }
  return steps;
}

int getsteps2(std::vector<int> list)
{
  int pos = 0, steps = 0, prev;
  while (pos < list.size())
  {
    prev = pos;
    pos = pos + list.at(pos);
    if (list.at(prev) >= 3)
    {
      list.at(prev) -= 1;
    }
    else
    {
      list.at(prev) += 1;
    }
    steps += 1;
  }
  return steps;
}