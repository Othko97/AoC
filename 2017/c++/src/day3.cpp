#include <iostream>   //cout
#include <cstdlib>    //abs
#include <vector>     //vector
#include <cmath>      //floor, sqrt
#include <algorithm>  //sort

//Prototypes
std::vector<int> getcoordinates(int x);
int invcoordinates(std::vector<int> coords);
int manhattan(std::vector<int> vec1, std::vector<int> vec2);
int hausdorff(std::vector<int> vec1, std::vector<int> vec2);
std::vector<int> getadjacents(int x);
int getvalue(int x, int y, std::vector<int> vals);
int writevalue(int x, std::vector<int> vals);






//Main
int main()
{
  int input = 312051;
  std::vector<int> origin = {0,0};

  std::cout << manhattan(getcoordinates(input), origin) << std::endl;
  
  std::vector<int> vals = {1};
  int i = 2;
  while (vals[vals.size()-1] <= input)
  {
    vals.push_back(writevalue(i, vals));
    //std::cout << vals[vals.size()-1] << std::endl;
    i++;
  }
  std::cout << vals[vals.size()-1] << std::endl;
  return 0;
}






//Function Definitions
std::vector<int> getcoordinates(int x)
{
  std::vector<int> origin = {0,0};
  if (x == 1) {return origin;}

  int sqwidth = (int) floor(sqrt(x));
  if (sqwidth % 2 == 0) {sqwidth -= 1;}
  int corner = sqwidth * sqwidth;
    
  int step = sqwidth;
  
  if (x != corner) 
  {
    step += 1;
  }
  else
  {
    step -= 1;
  }

  x -= corner;
  int quotient = (int) ((x - (x % step)) / (step));
  std::vector<int> coords;

  if (quotient == 0) {coords = {step, x % (step)};}
  if (quotient == 1) {coords = {step - (x % (step)), step};}
  if (quotient == 2) {coords = {0, step - (x % step)};}
  if (quotient == 3) {coords = {x % step, 0};}

  coords[0] -= (int) step / 2;
  coords[1] -= (int) step / 2;

  return coords;
}

int invcoordinates(std::vector<int> coords)
{
  std::vector<int> origin = {0,0};
  if (coords == origin) {return 1;}

  int step = 2 * hausdorff(coords, origin);
  int corner = (step - 1) * (step - 1);
  coords[0] += (int) step / 2;
  coords[1] += (int) step / 2;
  int quotient, rem;

  if (coords[0] == step && coords[1] > 0) {quotient = 0; rem = coords[1];}
  if (coords[1] == step && coords[0] < step) {quotient = 1; rem = step - coords[0];};
  if (coords[0] == 0 && coords[1] < step) {quotient = 2; rem = step - coords[1];}
  if (coords[1] == 0 && coords[0] > 0) {quotient = 3; rem = coords[0];}

  return corner + (quotient * step) + rem;
}

int manhattan (std::vector<int> vec1, std::vector<int> vec2)
{
  return std::abs(vec1[0] - vec2[0]) + std::abs(vec1[1] - vec2[1]);
}

int hausdorff(std::vector<int> vec1, std::vector<int> vec2)
{
  return (abs(vec1[0] - vec2[0]) >= abs(vec1[1] - vec2[1])) ? abs(vec1[0] - vec2[0]) : abs(vec1[1] - vec2[1]);
}

std::vector<int> getadjacents(int x)
{
  std::vector<int> coords = getcoordinates(x);
  std::vector<int> adjs;

  for (int i = -1; i <= 1; i++)
  {
    for (int j = -1; j <= 1; j++)
    {
      if (i != 0 || j != 0)
      {
        std::vector<int> adjcoords = {coords[0] + i, coords[1] + j};
        adjs.push_back(invcoordinates(adjcoords));
      }
    }
  }
  std::sort(adjs.begin(), adjs.end());
  return adjs;
}

int getvalue(int x, int y, std::vector<int> vals)
{
  if (y >= x)
  {
    return 0;
  }
  else
  {
    return vals[y-1];
  }
}

int writevalue(int x, std::vector<int> vals)
{
  if (vals.size() == 0 && x == 1)
  {
    return 1;
  }

  std::vector<int> adjs = getadjacents(x);
  int sum = 0;
  for (int i = 0; i < adjs.size(); i++)
  {
    sum += getvalue(x, adjs[i], vals);
  }
  return sum;
}