//https://www.hackerrank.com/challenges/dynamic-array/problem

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static int lastAnswer = 0;
    public static List<int> results = new List<int>();

    public static List<int> dynamicArray(int n, List<List<int>> queries)
    {
        List<List<int>> twoDimensionalArray = new List<List<int>>();

        //creating a 2d array
        for (int i = 0; i < n; i++)
        {
            twoDimensionalArray.Add(new List<int>());
        }

        foreach (List<int> query in queries)
        {
            ExecuteQuery(query, twoDimensionalArray, n);
        }

        return results;
    }

    public static void ExecuteQuery(List<int> query, List<List<int>> dArray, int n)
    {
        switch (query[0])
        {
            case 1:
                QueryTypeOne(query, dArray, n);
                break;
            case 2:
                QueryTypeTwo(query, dArray, n);
                break;
        }
    }

    public static void QueryTypeOne(List<int> query, List<List<int>> dArray, int n)
    {
        int x = query[1];
        int y = query[2];

        int index = ((x ^ lastAnswer) % n);

        dArray.ElementAt(index).Add(y);
    }

    public static void QueryTypeTwo(List<int> query, List<List<int>> dArray, int n)
    {
        int x = query[1];
        int y = query[2];

        int index = ((x ^ lastAnswer) % n);

        int size = dArray.ElementAt(index).Count;

        int value = y % size;

        lastAnswer = dArray.ElementAt(index).ElementAt(value);

        results.Add(lastAnswer);
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        int n = Convert.ToInt32(firstMultipleInput[0]);

        int q = Convert.ToInt32(firstMultipleInput[1]);

        List<List<int>> queries = new List<List<int>>();

        for (int i = 0; i < q; i++)
        {
            queries.Add(Console.ReadLine().TrimEnd().Split(' ').ToList().Select(queriesTemp => Convert.ToInt32(queriesTemp)).ToList());
        }

        List<int> result = Result.dynamicArray(n, queries);

        textWriter.WriteLine(String.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
