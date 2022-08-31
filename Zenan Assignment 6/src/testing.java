import java.util.Scanner;
import java.util.StringTokenizer;

public class testing {
	public static final double INFINITY = Double.MAX_VALUE;
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String line2 = "1 1";
		System.out.println(line2.indexOf(":"));
		
		int num = Integer.parseInt(scanner.nextLine());
		Graph g = new Graph();
		 
		for (int I = 0; I < num; I++) {
			String input = scanner.nextLine();
			StringTokenizer st = new StringTokenizer(input);
			String source = st.nextToken();
			while (st.hasMoreTokens()) {
				String dest = st.nextToken();
				int cost = Integer.parseInt( st.nextToken() );
				g.addEdge(source, dest, cost);
			}
		}
		
		Integer numberOfDrivers = Integer.parseInt(scanner.nextLine());
		String line = scanner.nextLine();
		String[] arrDriverHome = line.split(" ");
		int DeliveryRequested = Integer.parseInt(scanner.nextLine());
		line = scanner.nextLine();
		
		StringTokenizer st = new StringTokenizer(line);
		String[][] Delivery = new String[DeliveryRequested][3];;

		for (int i = 0; i < DeliveryRequested; i++) {
			Delivery[i][0] = Integer.toString(i);
			Delivery[i][1] = st.nextToken();
			Delivery[i][2] = st.nextToken();
		}
		String[] Delivery2 = line.split(" ");
		String[] arrPickup = new String[Delivery2.length / 2];
		String[] arrDropoff = new String[Delivery2.length / 2];
		
		for (int I = 0; (int)(Delivery2.length / 2) > I ; I++) {
			arrPickup[I] = Delivery2[I*2];
			arrDropoff[I] = Delivery2[I*2 + 1];
		}
		g.dijkstra("2");
		System.out.println(g.getPath("3"));

	}

}
