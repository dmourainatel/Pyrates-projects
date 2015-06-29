/*
  This app is an example of c# call python

  The starcore libraries linked is trail version.
  You can get release version from windows phone store.
  Thanks for support, if there are any question, please contact:
  srplab.cn@gmail.com
  li9416@gmail.com
*/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using call_python_example.Resources;

using libstarcore;
using star_csharp45;

namespace call_python_example
{
    public partial class MainPage : PhoneApplicationPage
    {
        private dynamic python;
        // Constructor
        public MainPage()
        {
            InitializeComponent();

            // Sample code to localize the ApplicationBar
            //BuildLocalizedApplicationBar();
            inputbox.Text = "" +
                "def add(a,b) :\n" +
                "    return a+b\n" +
                "g1 = 123\n" +
                "para = \"hello\"\n" +
                "c=[123,456]\n";

            //---init starcore
            StarCoreFactoryInit.Init();
            StarCoreFactory starcore = StarCoreFactory.GetFactory();
            StarServiceClass Service = (StarServiceClass)starcore._InitSimple("test", "123", 0, 0, null);
            StarSrvGroupClass SrvGroup = (StarSrvGroupClass)Service._Get("_ServiceGroup");

            //--init python raw interface ---*/
            SrvGroup._InitRaw("python", Service);
            //--getpython global object ---*/
            python = Service._ImportRawContext("python", "", false, "");
            //--run script of inputbox;
            python.execute(inputbox.Text);
            //--load python file---*/
            python.executefile(Windows.ApplicationModel.Package.Current.InstalledLocation.Path + "\\test.py");
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            /*---set value of python variable para---*/
            python.para = parabox.Text;
            string outtext = "";
            /*---get value of python variable g1---*/
            outtext += "get python value g1 : = " + (int)python.g1 + "\n";
            /*---get value of python variable para1---*/
            outtext += "get python value para : = " + (string)python.para + "\n";
            /*---call python function add---*/
            outtext += "call python function add(12,34) : = " + (int)python.add(12, 34) + "\n";
            /*---call python function tt of test.python---*/
            outtext += "call python function tt(12,34) : = " + (int)python.tt(12, 34) + "\n";
            /*---get value of python variable c, which is a table---*/
            dynamic c = python.c;
            outtext += "get python value c[0] : = " + (int)c[0] + "\n";
            outtext += "get python value c[1] : = " + (int)c[1] + "\n";
            /*---call python _Eval function for python code segment---*/
            outtext += "python.eval(\"2*2\") = " + (int)python.eval("2*2") + "\n";

            outputbox.Text = outtext;
        }

        // Sample code for building a localized ApplicationBar
        //private void BuildLocalizedApplicationBar()
        //{
        //    // Set the page's ApplicationBar to a new instance of ApplicationBar.
        //    ApplicationBar = new ApplicationBar();

        //    // Create a new button and set the text value to the localized string from AppResources.
        //    ApplicationBarIconButton appBarButton = new ApplicationBarIconButton(new Uri("/Assets/AppBar/appbar.add.rest.png", UriKind.Relative));
        //    appBarButton.Text = AppResources.AppBarButtonText;
        //    ApplicationBar.Buttons.Add(appBarButton);

        //    // Create a new menu item with the localized string from AppResources.
        //    ApplicationBarMenuItem appBarMenuItem = new ApplicationBarMenuItem(AppResources.AppBarMenuItemText);
        //    ApplicationBar.MenuItems.Add(appBarMenuItem);
        //}
    }
}