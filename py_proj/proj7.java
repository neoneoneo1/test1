import com.sun.xml.internal.ws.wsdl.writer.document.Import;
import sun.org.mozilla.javascript.internal.JavaScriptException;
import sun.security.krb5.Config;
import javax.annotation.processing.FilerException;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import javax.swing.plaf.basic.BasicInternalFrameTitlePane;
import javax.swing.table.TableColumn;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.MutableTreeNode;
import javax.swing.tree.TreeNode;
import javax.tools.JavaCompiler;
import javax.xml.crypto.Data;
import java.beans.XMLDecoder;
import java.beans.XMLEncoder;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.IntBuffer;
import java.nio.channels.Channel;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.CharsetEncoder;
import java.nio.charset.CodingErrorAction;
import java.security.*;
import java.security.PublicKey;
import java.util.*;
import java.util.concurrent.ConcurrentNavigableMap;
import java.util.prefs.Preferences;
import java.util.regex.*;
import java.text.*;
import java.lang.reflect.*;
import java.net.*;
import java.io.*;
import java.security.*;
import java.util.zip.*;
import java.security.cert.*;
import javax.net.ssl.*;
import java.util.prefs.Preferences;
import java.util.logging.*;
import java.nio.*;
import java.nio.channels.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class proj7 extends JFrame
{
    public proj7()
    {
        setTitle("Simple example");
        setSize(800, 600);
        setLocationRelativeTo(null);

        JPanel panel=new JPanel();
        getContentPane().add(panel);

        JLabel lbl1=new JLabel("JLabel");

        JButton bu1=new JButton("JButton");

        JToggleButton tog1=new JToggleButton("JToggleButton");

        JCheckBox chk1=new JCheckBox("JCheckBox");

        JRadioButton rad1=new JRadioButton("JRadioButton");
        JRadioButton rad2=new JRadioButton("JRadioButton");
        ButtonGroup grp1=new ButtonGroup();
        grp1.add(rad1);
        grp1.add(rad2);

        JComboBox jcombo=new JComboBox();
        jcombo.addItem("one");
        jcombo.addItem("two");

        String items[]={"item1","item2","item3"};
        JList jl1=new JList(items);

        JList jl2=new JList();
        DefaultListModel modl1=new DefaultListModel();
        modl1.addElement("item1");
        modl1.addElement("item2");
        modl1.addElement("item3");
        jl2.setModel(modl1);

        JTextField txtField=new JTextField();
        txtField.setText("dgdfgfg");

        JTextArea txtArea=new JTextArea();
        txtArea.setText("dgdfgfg");
        txtArea.setRows(3);
        txtArea.setColumns(10);

        JScrollBar scrl=new JScrollBar();

        JSlider sldr=new JSlider();

        JProgressBar progrs=new JProgressBar();
        progrs.setMaximum(10);
        progrs.setValue(5);

        JFormattedTextField txtfrmt=new JFormattedTextField();
        txtfrmt.setColumns(10);

        JPasswordField pas=new JPasswordField();
        pas.setColumns(10);

        JSpinner spin=new JSpinner();

        JSeparator jsep=new JSeparator();

        JTextPane txtPane=new JTextPane();
        txtPane.setSize(100,100);
        txtPane.setText("dfgdfggdg\nsdfsdfsd");

        JEditorPane jedit=new JEditorPane();
        jedit.setText("ggd\nfdgfsdf");

        DefaultMutableTreeNode root = new DefaultMutableTreeNode("Root");
        DefaultMutableTreeNode child1 = new DefaultMutableTreeNode("Child 1");
        root.add(child1);
        DefaultMutableTreeNode child2 = new DefaultMutableTreeNode("Child 2");
        root.add(child2);
        JTree tree = new JTree(root);

        Object colNames[]=    {"col1","col2","col3"};
        Object rowData[][]={    {"item r1,c1","item r1 c1","item r1 c3"},
                                {"item r2,c1","item r2 c1","item r2 c3"},
                                {"item r3,c1","item r3 c1","item r3 c3"} };
        JTable table1=new JTable(rowData,colNames);


        JLabel lblInTab=new JLabel("lbl in tab");
        JLabel lblInTab2=new JLabel("lbl2 in tab");
        JTabbedPane tabs=new JTabbedPane();
        tabs.setSize(200,200);
        tabs.addTab("tab1",lblInTab);
        tabs.addTab("tab2",lblInTab2);

        JLabel lblSplit1=new JLabel("lblSplit1");
        JLabel lblSplit2=new JLabel("lblSplit2");
        JPanel pan1=new JPanel();
        JSplitPane splitter=new JSplitPane();
        splitter.setLeftComponent(lblSplit1);
        splitter.setRightComponent(lblSplit2);
        pan1.add(splitter);


        JPanel panForScroll=new JPanel();
        JEditorPane jedit1=new JEditorPane();
        jedit1.setText("ggd\nfdgfsdf");
        JScrollPane srclPan=new JScrollPane();
        srclPan.getViewport().add(jedit1);
        panForScroll.add(srclPan, BorderLayout.CENTER);

        JToolBar toolBr=new JToolBar();
        JButton jbnToolbarButtons = new JButton("button on toolbar or image");
		jbnToolbarButtons.setToolTipText("left");
		jbnToolbarButtons.addActionListener
        (
            new ActionListener()
            {
                public void actionPerformed(ActionEvent e)
                {
                    //TODO
                }
		    }
        );
        toolBr.add(jbnToolbarButtons);

        JDesktopPane deskPane=new JDesktopPane();
        boolean resizable = true;
        boolean closeable = true;
        boolean maximizable  = true;
        boolean iconifiable = false;
        JInternalFrame iframe = new JInternalFrame("Frame Title", resizable, closeable, maximizable, iconifiable);
        iframe.setBounds(0, 0, 300, 150);
        iframe.setVisible(true);
        iframe.setSize(200, 50);
        iframe.getContentPane().add(new JTextArea());
        iframe.pack();
        deskPane.add(iframe);
        iframe.setVisible(true);
        //add(deskPane);

        JLayeredPane layPan=new JLayeredPane();
        JInternalFrame iframe1 = new JInternalFrame("Frame Title1", resizable, closeable, maximizable, iconifiable);
        JInternalFrame iframe2 = new JInternalFrame("Frame Title2", resizable, closeable, maximizable, iconifiable);
        JInternalFrame iframe3 = new JInternalFrame("Frame Title3", resizable, closeable, maximizable, iconifiable);
        iframe1.setVisible(true);
        iframe1.setBounds(50, 50, 100, 100);
        iframe1.getContentPane().add(new JLabel("if1"), BorderLayout.CENTER);
        iframe2.setVisible(true);
        iframe2.setBounds(170, 50, 100, 100);
        iframe2.getContentPane().add(new JLabel("if2"), BorderLayout.CENTER);
        iframe3.setVisible(true);
        iframe3.setBounds(350, 50, 100, 100);
        iframe3.getContentPane().add(new JLabel("if2"), BorderLayout.CENTER);
        layPan.setOpaque(false);
        layPan.add(iframe1, JLayeredPane.POPUP_LAYER);
        layPan.add(iframe2, JLayeredPane.DEFAULT_LAYER);
        layPan.add(iframe3, JLayeredPane.PALETTE_LAYER);
        //add(layPan, BorderLayout.CENTER);
        layPan.setVisible(true);

        panel.add(lbl1);
        panel.add(bu1);
        panel.add(tog1);
        panel.add(chk1);
        panel.add(rad1);
        panel.add(rad2);
        panel.add(jcombo);
        panel.add(jl1);
        panel.add(jl2);
        panel.add(txtField);
        panel.add(txtArea);
        panel.add(scrl);
        panel.add(sldr);
        panel.add(progrs);
        panel.add(txtfrmt);
        panel.add(pas);
        panel.add(spin);
        panel.add(jsep);
        panel.add(txtPane);
        panel.add(jedit);
        panel.add(tree);
        panel.add(table1);
        panel.add(tabs);
        panel.add(pan1);
        panel.add(panForScroll);
        panel.add(toolBr);




        setVisible(true);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    public static void main(String pars[]) throws IOException, NoSuchAlgorithmException
    {
        SwingUtilities.invokeLater
        (
            new Runnable()
            {
                public void run()
                {
                    proj7 ex = new proj7();
                }
            }
        );
    }
}

