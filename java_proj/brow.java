import org.eclipse.jface.window.ApplicationWindow;
import org.eclipse.swt.widgets.Display;

public class brow extends ApplicationWindow {

public static void main(String[] args) 
{
	brow window = new brow(); // ������� ���� ����
	window.setBlockOnOpen( true ); // ������������� ���� - ����� �������� ����
	window.open(); // ��������� ����
	Display.getCurrent().dispose(); // ����������� �������
}

public brow() 
{
	super( null ); // �������� ����������� ������������� ������
}

}
/*
import org.eclipse.jface.window.ApplicationWindow;
import org.eclipse.jface.*;
import org.eclipse.jface.window.*;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.*;
 
public class brow extends ApplicationWindow 
{
  public brow() 
  {
    super(null);
  }
  public void run() {
    setBlockOnOpen(true);
    open();
    Display.getCurrent().dispose();
  }
  protected Control createContents(Composite parent) 
  {
    Label label = new Label(parent, SWT.CENTER);
    label.setText("Hello, World");
    return label;
  }
  public static void main(String[] args) 
  {
	  brow br=new brow();
	  br.run();
  }  
}




import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.browser.*;

public class brow {
     public static void main(String[] args) {
      //������� ������ Display ��� ����� SWT
      //� �������� ������������ �������
        Display display = new Display();
        //������� ���� ���������
        Shell shell = new Shell(display);
        //shell.setText("SWT Hello");
        shell.setSize(1000, 500);
        Browser browser;
        try {
           browser = new Browser(shell,SWT.NO);
           browser.setUrl("http://www.mvstroy.ru");
           browser.setSize(1000,500);
        }        
        catch (Exception e) 
        {
           System.exit(-1);
        }        
        
        shell.open();
        //��������� �������� ����
        while (!shell.isDisposed())
        {
          if (!display.readAndDispatch()) {
                display.sleep();
            }
        }
        //������� ������������ �������
        //������ ���� ����������� 
        display.dispose();
    }
} 
*/