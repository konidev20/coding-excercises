using System.Collections.Generic;

namespace CodingPractice
{
    public class Stack
    {
        private int count { get; set; } = 0;
        private Queue<int> queueOne { get; set; } = new Queue<int>();
        private Queue<int> queueTwo { get; set; } = new Queue<int>();

        /// <summary>
        /// Here we are making the push operation complex.
        /// </summary>
        /// <param name="d"></param>
        public void Push(int d) {
            count++;
            queueTwo.Enqueue(d);
            
            while(queueTwo.Count > 0) 
            {
                int temp = queueOne.Dequeue();
                queueTwo.Enqueue(temp);
            }

            Queue<int> tempQueue = queueOne;
            queueOne = queueTwo;
            queueTwo = tempQueue;
        }

        /// <summary>
        /// Pop Operation will just dequeue the last element in the queue.
        /// </summary>
        /// <param name="d"></param>
        /// <returns></returns>
        public int Pop(int d) {
            count--;
            return queueOne.Dequeue();
        }
    }
}
