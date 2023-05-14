using Microsoft.Office.Interop.Excel;
using ExcelDataReader;
using Newtonsoft.Json;
using System.Text;

namespace CSViewer
{
    public partial class Form1 : Form
    {
        private const int INDEX_ID = 0;
        private const int INDEX_DATE = 2;
        private const int INDEX_URL = 3;
        private const int INDEX_HEADLINE = 4;
        private const int INDEX_CONTENT = 5;

        private List<Entry> entries;
        public Form1()
        {
            InitializeComponent();
            System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
            entries = new();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // populate the information on the side
            Entry entry = (Entry)listBox1.SelectedItem;

            headlineTexBox.Text = entry.Headline;
            URLTextBox.Text = entry.Url;
            contentBox.Text = entry.Content;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Filter = "Excel Files|*.xls;*.xlsx;*.xlsm"
            };

            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                using (var stream = File.Open(openFileDialog.FileName, FileMode.Open, FileAccess.Read))
                {
                    using (var reader = ExcelReaderFactory.CreateReader(stream, new ExcelReaderConfiguration()
                    {
                        FallbackEncoding = Encoding.GetEncoding(1252)
                    }))
                    {
                        while (reader.Read()) // Each ROW
                        {
                            if (reader.GetValue(INDEX_ID).ToString() == "article_id") continue; // skip the first row (header)

                            string tag = reader.GetValue(INDEX_ID).ToString();

                            string jsonContent = reader.GetValue(INDEX_CONTENT)?.ToString();

                            string headline = reader.GetValue(INDEX_HEADLINE)?.ToString();
                            string url = reader.GetValue(INDEX_URL)?.ToString();

                            List<string> content = new();
                            content.Append(jsonContent);
                            entries.Add(new Entry(tag, jsonContent, headline, url));
                        }
                    }
                }

                listBox1.DataSource = entries;
            }
        }
    }
}