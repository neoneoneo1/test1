import org.eclipse.jface.window.ApplicationWindow;
import org.eclipse.swt.widgets.Display;

public class brow extends ApplicationWindow {

public static void main(String[] args) 
{
	brow window = new brow(); // Создаем наше окно
	window.setBlockOnOpen( true ); // Устанавливаем флаг - ждать закрытия окна
	window.open(); // Открываем окно
	Display.getCurrent().dispose(); // Освобождаем ресурсы
}

public brow() 
{
	super( null ); // Вызываем конструктор родительского класса
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
      //Создаем объект Display для связи SWT
      //С дисплеем операционной системы
        Display display = new Display();
        //Создаем окно программы
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
        //Обработка закрытия окна
        while (!shell.isDisposed())
        {
          if (!display.readAndDispatch()) {
                display.sleep();
            }
        }
        //Ресурсы операционной системы
        //должны быть освобождены 
        display.dispose();
    }
} 
*/