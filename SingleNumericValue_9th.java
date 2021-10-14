import javax.swing.*;
import javax.swing.text.AttributeSet.ColorAttribute;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SingleNumericValue_9th  {

    public static void main(String[] args) {
        String[] onedigit = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        JFrame f=new JFrame("Text Convert");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        final JTextField tf=new JTextField();
        tf.setBounds(50,50, 150,20);
        JButton b=new JButton("Click Here");
        b.setBounds(60,100,120,30);
        JLabel l = new JLabel("Answer = ");
        l.setBounds(60,130,150,30);

        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                String s = tf.getText();
                if (s.matches("\\d") && s.length()==1)
                {
                    tf.setBackground(Color.GREEN);
                    Integer i = Integer.parseInt(s);
                    l.setText("Answer = "+onedigit[i]);
                    l.setForeground(Color.BLACK);
                }
                else{
                    tf.setBackground(Color.RED);
                    l.setText("Enter a single digit");
                    l.setForeground(Color.RED);
                }

            }
        });
        f.add(b);f.add(tf);f.add(l);
        f.setSize(400,400);
        f.setLayout(null);
        f.setVisible(true);
    }
}
