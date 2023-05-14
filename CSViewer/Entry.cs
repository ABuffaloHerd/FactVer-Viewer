using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace CSViewer
{
    internal class Entry
    {
        //public List<string> Content { get; private set; }
        public string Content { get; private set; } // fuckinwork
        public string Url { get; private set; }
        public string Headline { get; private set; }

        public string Tag { get; private set; }

        //public Entry(string Tag, List<string> content, string headline, string url)
        //{
        //    this.Tag = Tag;
        //    Content = content;
        //    Headline = headline;
        //    Url = url;
        //}

        public Entry(string tag, string content, string headline, string url)
        {
            Tag = tag;
            Content = content;
            Headline = headline;
            Url = url;
        }

        public override string ToString()
        {
            return Headline;
        }
    }
}
