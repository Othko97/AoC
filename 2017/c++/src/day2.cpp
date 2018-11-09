#include <iostream>   //cout
#include <fstream>    //ifstream
#include <string>     //string
#include <sstream>    //stringstream
#include <vector>     //vector
#include <climits>    //INT_MIN, INT_MAX


//Functions
int checksum1(std::vector< std::vector<int> > &table);
int checksum2(std::vector< std::vector<int> > &table);
int max(std::vector<int> &row);
int min(std::vector<int> &row);
bool divisible(int a, int b);


int main()
{
  //Variables
  std::ifstream data ("../data/day2.txt");
  std::string line;
  std::vector< std::vector<int> > table;

  if (data.is_open())
  {
    while (getline(data, line))
    {
      std::vector<int> row;
      std::stringstream stream(line);
      for (int line; stream >> line;)
      {
        row.push_back(line);
      }
      table.push_back(row);
    }
  }

  std::cout << "First Checksum: " << checksum1(table) << std::endl;
  std::cout << "Second Checksum: " << checksum2(table) << std::endl;
  return 0;
}

int checksum1(std::vector< std::vector<int> > &table)
{
  int sum = 0;
  for (int i = 0; i < table.size(); i++)
  {
    sum += max(table[i]) - min(table[i]);
  }
  return sum;
}

int checksum2(std::vector< std::vector<int> > &table)
{
  int sum = 0;
  for (int i = 0; i < table.size(); i++)
  {
    for (int j = 0; j < table[i].size(); j++)
    {
      for (int k = 0; k < table[i].size(); k++)
      {
        if (divisible(table[i][k], table[i][j]))
        {
          sum += (int)table[i][j]/table[i][k];
        }
      }
    }
  }
  return sum;
}

int max(std::vector<int> &row)
{
  int max = INT_MIN;
  for (int i : row)
  {
    if (i > max)
      max = i;
  }
  return max;
}

int min(std::vector<int> &row)
{
  int min = INT_MAX;
  for (int i : row)
  {
    if (i < min)
      min = i;
  }
  return min;
}

bool divisible(int a, int b)
{
  return (a != b) && (b % a == 0);
}