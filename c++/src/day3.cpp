#include <iostream>   //cout
#include <cstdlib>    //abs
#include <vector>     //vector
#include <cmath>      //floor, sqrt

//Prototypes
std::vector<int> getcoordinates(int x);
int invcoordinates(std::vector<int> coords);
int manhattan(std::vector<int> vec1, std::vector<int> vec2);
int hausdorff(std::vector<int> vec1, std::vector<int> vec2);
int getvalue(int x, int y, std::vector<int> vals);
int writevalue(int x, std::vector<int> vals);

//Main
int main()
{
  int input = 312051;
  std::vector<int> origin = {0,0};

  for (int i = 1; i < 35; i++)
  {
    std::vector<int> x = getcoordinates(i);
    std::cout << i << "\t" << '(' << x[0] << ',' << x[1] << ")\t"  << manhattan(x, origin) << "\t" << hausdorff(x, origin) << std::endl;
  }

  std::cout << manhattan(getcoordinates(input), origin);
  return 0;
}


//Function Definitions
std::vector<int> getcoordinates(int x)
{
  std::vector<int> origin = {0,0};
  if (x == 1) {return origin;}

  int sqwidth = (int) floor(sqrt(x));
  int corner = sqwidth * sqwidth;
  int step = sqwidth;
  if (sqwidth % 2 == 1)
  {
    if (x == corner)
    {
      step -= 1;
    }
    else
    {
      step += 1;
    }
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
  int step = 2 * hausdorff(coords, origin);
  coords[0] += (int) step / 2;
  coords[1] += (int) step / 2;
  int quotient;
  if (coords[0] == step && coords[1] > 0) {quotient = 1;}
  if (coords[1] == step && 1)
  if (coords[0] == 0 && coords[1] < step) {quotient = 2;}
  if (coords[1] == 0 && coords[0] > 0) {quotient = 3;}
}

int manhattan (std::vector<int> vec1, std::vector<int> vec2)
{
  return std::abs(vec1[0] - vec2[0]) + std::abs(vec1[1] - vec2[1]);
}

int hausdorff(std::vector<int> vec1, std::vector<int> vec2)
{
  return (abs(vec1[0] - vec2[0]) >= abs(vec1[1] - vec2[1])) ? abs(vec1[0] - vec2[0]) : abs(vec1[1] - vec2[1]);
}