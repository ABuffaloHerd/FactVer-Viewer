namespace CSViewer
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            listBox1 = new ListBox();
            headlineTexBox = new TextBox();
            label1 = new Label();
            label3 = new Label();
            toolStrip1 = new ToolStrip();
            toolStripDropDownButton1 = new ToolStripDropDownButton();
            openToolStripMenuItem = new ToolStripMenuItem();
            toolStripDropDownButton2 = new ToolStripDropDownButton();
            filterToolStripMenuItem = new ToolStripMenuItem();
            disableFiltersToolStripMenuItem = new ToolStripMenuItem();
            URLTextBox = new TextBox();
            label4 = new Label();
            contentBox = new RichTextBox();
            articleBox = new TextBox();
            label2 = new Label();
            copyIDButton = new Button();
            toolStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // listBox1
            // 
            listBox1.FormattingEnabled = true;
            listBox1.ItemHeight = 15;
            listBox1.Location = new Point(12, 28);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(490, 724);
            listBox1.TabIndex = 0;
            listBox1.SelectedIndexChanged += listBox1_SelectedIndexChanged;
            // 
            // headlineTexBox
            // 
            headlineTexBox.BorderStyle = BorderStyle.FixedSingle;
            headlineTexBox.Location = new Point(570, 57);
            headlineTexBox.Name = "headlineTexBox";
            headlineTexBox.ReadOnly = true;
            headlineTexBox.Size = new Size(886, 23);
            headlineTexBox.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(510, 60);
            label1.Name = "label1";
            label1.Size = new Size(54, 15);
            label1.TabIndex = 2;
            label1.Text = "Headline";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(508, 118);
            label3.Name = "label3";
            label3.Size = new Size(55, 15);
            label3.TabIndex = 2;
            label3.Text = "Contents";
            label3.Click += label2_Click;
            // 
            // toolStrip1
            // 
            toolStrip1.Items.AddRange(new ToolStripItem[] { toolStripDropDownButton1, toolStripDropDownButton2 });
            toolStrip1.Location = new Point(0, 0);
            toolStrip1.Name = "toolStrip1";
            toolStrip1.Size = new Size(1485, 25);
            toolStrip1.TabIndex = 4;
            toolStrip1.Text = "toolStrip1";
            // 
            // toolStripDropDownButton1
            // 
            toolStripDropDownButton1.DisplayStyle = ToolStripItemDisplayStyle.Text;
            toolStripDropDownButton1.DropDownItems.AddRange(new ToolStripItem[] { openToolStripMenuItem });
            toolStripDropDownButton1.Image = (Image)resources.GetObject("toolStripDropDownButton1.Image");
            toolStripDropDownButton1.ImageTransparentColor = Color.Magenta;
            toolStripDropDownButton1.Name = "toolStripDropDownButton1";
            toolStripDropDownButton1.Size = new Size(38, 22);
            toolStripDropDownButton1.Text = "File";
            // 
            // openToolStripMenuItem
            // 
            openToolStripMenuItem.Name = "openToolStripMenuItem";
            openToolStripMenuItem.Size = new Size(103, 22);
            openToolStripMenuItem.Text = "Open";
            openToolStripMenuItem.Click += openToolStripMenuItem_Click;
            // 
            // toolStripDropDownButton2
            // 
            toolStripDropDownButton2.DisplayStyle = ToolStripItemDisplayStyle.Text;
            toolStripDropDownButton2.DropDownItems.AddRange(new ToolStripItem[] { filterToolStripMenuItem, disableFiltersToolStripMenuItem });
            toolStripDropDownButton2.Image = (Image)resources.GetObject("toolStripDropDownButton2.Image");
            toolStripDropDownButton2.ImageTransparentColor = Color.Magenta;
            toolStripDropDownButton2.Name = "toolStripDropDownButton2";
            toolStripDropDownButton2.Size = new Size(45, 22);
            toolStripDropDownButton2.Text = "View";
            // 
            // filterToolStripMenuItem
            // 
            filterToolStripMenuItem.Name = "filterToolStripMenuItem";
            filterToolStripMenuItem.Size = new Size(146, 22);
            filterToolStripMenuItem.Text = "Filter";
            filterToolStripMenuItem.Click += filterToolStripMenuItem_Click;
            // 
            // disableFiltersToolStripMenuItem
            // 
            disableFiltersToolStripMenuItem.Name = "disableFiltersToolStripMenuItem";
            disableFiltersToolStripMenuItem.Size = new Size(146, 22);
            disableFiltersToolStripMenuItem.Text = "Disable Filters";
            disableFiltersToolStripMenuItem.Click += disableFiltersToolStripMenuItem_Click;
            // 
            // URLTextBox
            // 
            URLTextBox.BorderStyle = BorderStyle.FixedSingle;
            URLTextBox.Location = new Point(570, 86);
            URLTextBox.Name = "URLTextBox";
            URLTextBox.ReadOnly = true;
            URLTextBox.Size = new Size(886, 23);
            URLTextBox.TabIndex = 1;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(510, 89);
            label4.Name = "label4";
            label4.Size = new Size(28, 15);
            label4.TabIndex = 2;
            label4.Text = "URL";
            label4.Click += label2_Click;
            // 
            // contentBox
            // 
            contentBox.Location = new Point(569, 115);
            contentBox.Name = "contentBox";
            contentBox.ReadOnly = true;
            contentBox.Size = new Size(887, 637);
            contentBox.TabIndex = 5;
            contentBox.Text = "";
            // 
            // articleBox
            // 
            articleBox.BorderStyle = BorderStyle.FixedSingle;
            articleBox.Location = new Point(569, 28);
            articleBox.Name = "articleBox";
            articleBox.ReadOnly = true;
            articleBox.Size = new Size(736, 23);
            articleBox.TabIndex = 1;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(510, 30);
            label2.Name = "label2";
            label2.Size = new Size(55, 15);
            label2.TabIndex = 2;
            label2.Text = "Article ID";
            label2.Click += label2_Click_1;
            // 
            // copyIDButton
            // 
            copyIDButton.Location = new Point(1311, 28);
            copyIDButton.Name = "copyIDButton";
            copyIDButton.Size = new Size(145, 23);
            copyIDButton.TabIndex = 6;
            copyIDButton.Text = "Copy";
            copyIDButton.UseVisualStyleBackColor = true;
            copyIDButton.Click += copyIDButton_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1485, 762);
            Controls.Add(copyIDButton);
            Controls.Add(contentBox);
            Controls.Add(toolStrip1);
            Controls.Add(label3);
            Controls.Add(label4);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(URLTextBox);
            Controls.Add(articleBox);
            Controls.Add(headlineTexBox);
            Controls.Add(listBox1);
            Name = "Form1";
            Text = "FactVer Viewer";
            toolStrip1.ResumeLayout(false);
            toolStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ListBox listBox1;
        private TextBox headlineTexBox;
        private Label label1;
        private Label label3;
        private ToolStrip toolStrip1;
        private ToolStripDropDownButton toolStripDropDownButton1;
        private ToolStripMenuItem openToolStripMenuItem;
        private TextBox URLTextBox;
        private Label label4;
        private RichTextBox contentBox;
        private ToolStripDropDownButton toolStripDropDownButton2;
        private ToolStripMenuItem filterToolStripMenuItem;
        private ToolStripMenuItem disableFiltersToolStripMenuItem;
        private TextBox articleBox;
        private Label label2;
        private Button copyIDButton;
    }
}