using ExcelDataReader;
using System.Text;
using System.Text.RegularExpressions;

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
        private List<Entry> filteredEntries;
        public Form1()
        {
            InitializeComponent();
            System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
            entries = new();
            disableFiltersToolStripMenuItem.Enabled = false;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // populate the information on the side
            Entry entry = (Entry)listBox1.SelectedItem;

            headlineTexBox.Text = entry.Headline;
            URLTextBox.Text = entry.Url;
            contentBox.Text = entry.Content;
            articleBox.Text = entry.Tag;
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
                            content.Append(FilterJson(jsonContent));
                            entries.Add(new Entry(tag, FilterJson(jsonContent), headline, url));
                        }
                    }
                }

                listBox1.DataSource = entries;
            }
        }

        string FilterJson(string jsonContent)
        {
            string @fixed = jsonContent.Replace('[', ' ');
            string @fixed2 = @fixed.Replace(']', ' ');

            // regexes to clean up the fucked up mess that python scripts produce
            Regex rgx = new("\\\\n[\"'],\\s");
            Regex rgx2 = new("\\A[\\\"'][0-9]+:\\s");
            Regex rgx3 = new("\\\\n{0,}");
            Regex no_newlines = new("\\\\n");
            Regex fuck_off_leading_1 = new("[\"']1:\\s");

            string[] parts = rgx.Split(@fixed2);

            StringBuilder sb = new();
            foreach (string part in parts)
            {
                // remove anything that has the keyword 'adsbygoogle'
                if (part.Contains("adsbygoogle")) continue; // TODO: is this bogging down the load time?

                string clean = fuck_off_leading_1.Replace(part, "");
                sb.Append(rgx3.Replace(rgx2.Replace(clean, ""), "")).Append('\n');
            }

            return sb.ToString();
        }

        private void FilterEntries(string filter)
        {
            filteredEntries = new List<Entry>();
            foreach (Entry entry in entries)
            {
                if (entry.Tag.Contains(filter))
                {
                    filteredEntries.Add(entry);
                }
            }
            listBox1.DataSource = filteredEntries;
            disableFiltersToolStripMenuItem.Enabled = true;
        }

        private void DisableFilters()
        {
            listBox1.DataSource = entries;
        }

        private void filterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // ask for filter
            Form prompt = new Form()
            {
                Width = 500,
                Height = 150,
                FormBorderStyle = FormBorderStyle.FixedDialog,
                Text = "Enter filter string",
                StartPosition = FormStartPosition.CenterScreen
            };
            Label textLabel = new Label() { Left = 50, Top = 20, Text = "Filter" };
            TextBox textBox = new TextBox() { Left = 50, Top = 50, Width = 400 };
            Button confirmation = new Button() { Text = "Ok", Left = 350, Width = 100, Top = 90, DialogResult = DialogResult.OK };
            confirmation.Click += (sender, e) => { prompt.Close(); };
            prompt.Controls.Add(textBox);
            prompt.Controls.Add(confirmation);
            prompt.Controls.Add(textLabel);
            prompt.AcceptButton = confirmation;

            string filter = prompt.ShowDialog() == DialogResult.OK ? textBox.Text : "";
            if (filter.Length == 0) return;

            FilterEntries(filter);
        }

        private void disableFiltersToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DisableFilters();
            disableFiltersToolStripMenuItem.Enabled = false;
        }

        private void label2_Click_1(object sender, EventArgs e)
        {

        }

        private void copyIDButton_Click(object sender, EventArgs e)
        {
            if(articleBox.Text.Length == 0)
            {
                MessageBox.Show("I don't think you want to copy an empty string :|", "Are you sure about that?");
                return;
            }
            Clipboard.SetText(articleBox.Text);
        }
    }
}