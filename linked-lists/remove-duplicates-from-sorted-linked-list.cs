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

class Solution {

    class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    class SinglyLinkedList {
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;

        public SinglyLinkedList() {
            this.head = null;
            this.tail = null;
        }

        public void InsertNode(int nodeData) {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null) {
                this.head = node;
            } else {
                this.tail.next = node;
            }

            this.tail = node;
        }
    }

    static void PrintSinglyLinkedList(SinglyLinkedListNode node, string sep, TextWriter textWriter) {
        while (node != null) {
            textWriter.Write(node.data);

            node = node.next;

            if (node != null) {
                textWriter.Write(sep);
            }
        }
    }

    // Complete the removeDuplicates function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode removeDuplicates(SinglyLinkedListNode head) {
        SinglyLinkedListNode pointer = head;
        
        while(pointer.next != null){
            if(isNextNodeSame(pointer.data, pointer.next.data)){
                if (isNextNodeLast(pointer)){
                    pointer.next = null;
                    break;
                }
                pointer.next = pointer.next.next;
                continue;
            }
            pointer = pointer.next;
        }
        
        return head;
    }
    
    static bool isNextNodeLast(SinglyLinkedListNode node){
        return node.next.next == null ? true : false;
    }
    
    static bool isNextNodeSame(int current, int next){
        return current == next ? true : false;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            SinglyLinkedList llist = new SinglyLinkedList();

            int llistCount = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i < llistCount; i++) {
                int llistItem = Convert.ToInt32(Console.ReadLine());
                llist.InsertNode(llistItem);
            }

            SinglyLinkedListNode llist1 = removeDuplicates(llist.head);

            PrintSinglyLinkedList(llist1, " ", textWriter);
            textWriter.WriteLine();
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
