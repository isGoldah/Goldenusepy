using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("");
            Console.WriteLine("Enter your password");
            Console.WriteLine("");
            string userName = Console.ReadLine();
            if (userName == "Password")
            {
                Console.WriteLine("");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Welcome User!");
                Console.ForegroundColor = ConsoleColor.White;
                Console.WriteLine("");
                Console.WriteLine("Type the name of the app or game you need the Password.");
                Console.WriteLine("");
                string passmc = Console.ReadLine();
                if (passmc == "Minecraft")
                {
                    Console.WriteLine("The Minecraft password is Password.");
                }
                if (passmc == "Twitch")
                {
                    Console.WriteLine("The Twitch password is Password.");
                }
                if (passmc == "Steam")
                {
                    Console.WriteLine("The Steam password is Password.");
                }
                if (passmc == "GitHub")
                {
                    Console.WriteLine("The GitHub password is Password.");
                }
                
            }else
                Console.WriteLine("Wrong password");
                Console.ReadKey();
        }       
        }
    }



