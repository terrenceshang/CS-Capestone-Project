import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class SimulatorOne {
	public static final double INFINITY = Double.MAX_VALUE;
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
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
		String[] arrPickup = new String[(int)Delivery2.length / 2];
		String[] arrDropoff = new String[(int)Delivery2.length / 2];
		
		for (int I = 0; (int)(Delivery2.length / 2) > I ; I++) {
			arrPickup[I] = Delivery2[I*2];
			arrDropoff[I] = Delivery2[I*2 + 1];
		}
		try {
			String[][] arrHomePath = createPathArray(g, numberOfDrivers, arrDriverHome, DeliveryRequested, arrPickup);
			String[][] arrPickupPath = createPathArray(g, DeliveryRequested, arrPickup, DeliveryRequested, arrDropoff);
			String[][] arrDropoffPath = createPathArray(g, DeliveryRequested, arrDropoff, numberOfDrivers, arrDriverHome);
			
			String[][] arrHomePath2 = createPathArray2(g, numberOfDrivers, arrDriverHome, DeliveryRequested, arrPickup);
			String[][] arrPickupPath2 = createPathArray2(g, DeliveryRequested, arrPickup, DeliveryRequested, arrDropoff);
			String[][] arrDropoffPath2 = createPathArray2(g, DeliveryRequested, arrDropoff, numberOfDrivers, arrDriverHome);
			
			for (int I = 0; I < DeliveryRequested; I++) {
	            System.out.println("client "+Delivery[I][1] + " " + Delivery[I][2]);
	            double lowest = INFINITY;
	            String driver = "";
	            String dropoffPathFinal = "", pickupPathFinal = "", homePathFinal = "";
	            
	            for (int J = 0; J < numberOfDrivers; J++) {
	                double homePickupCost = Double.parseDouble(arrHomePath[J][I*2]);
	                double pickupDropoffCost = Double.parseDouble(arrPickupPath[I][2*I]);
	                double dropoffHomeCost = Double.parseDouble(arrDropoffPath[I][J*2]);
	                double totalCost = homePickupCost + pickupDropoffCost + dropoffHomeCost;
	                
	                String dropoffPath = "", pickupPath = "", homePath = "";
	                String dropoffPath2 = "", pickupPath2 = "", homePath2 = "";
	                if (totalCost >= INFINITY) {
	                	
	                } else {
	                	homePath = arrHomePath[J][2*I+1];
	                	pickupPath = arrPickupPath[I][2*I+1];
	                	dropoffPath = arrDropoffPath[I][2*J+1];
	                	homePath2 = arrHomePath2[J][2*I+1];
	                	pickupPath2 = arrPickupPath2[I][2*I+1];
	                	dropoffPath2 = arrDropoffPath2[I][2*J+1];
	                }
	                
	                if (totalCost < lowest) {
	                	lowest = totalCost;
	                	String tempHomePath = homePath + " ";
	                	driver = homePath.substring(0, tempHomePath.indexOf(" "));
	                	
	                	if (dropoffPath.equals(dropoffPath2)) {
	                		dropoffPathFinal = dropoffPath;
	                	} else {
	                		dropoffPathFinal = "multiple solutions cost " + Integer.toString((int)dropoffHomeCost);
	                	}
	                	
	                	if (pickupPath.equals(pickupPath2)) {
	                		pickupPathFinal = pickupPath;
	                	} else {
	                		pickupPathFinal = "multiple solutions cost " + Integer.toString((int)pickupDropoffCost);
	                	}
	                	
	                	if (homePath.equals(homePath2)) {
	                		homePathFinal = homePath;
	                	} else {
	                		homePathFinal = "multiple solutions cost " + Integer.toString((int)homePickupCost);
	                	}
	                	
	                }
	            }
	            
	            if (lowest >= INFINITY) {
	            	System.out.println("cannot be helped");
	            } else {
	            	System.out.println("truck " + driver);
	            	System.out.println(homePathFinal);
	            	System.out.println("pickup " + Delivery[I][1]);
	            	System.out.println(pickupPathFinal);
	            	System.out.println("dropoff " + Delivery[I][2]);
	            	System.out.println(dropoffPathFinal);
	            }
			}
		} catch(NoSuchElementException e) {
			System.out.println("client " + Delivery[0][1] + " " + Delivery[0][2]);
			System.out.println("cannot be helped");
		}
		
	}
    private static String[][] createPathArray(Graph g, int numStart, String[] startNodes, int numEnd, String[] endNodes) {
        String[][] arrPath  = new String [numStart][];
        for (int I = 0 ; I < numStart ; I++)
        {
            String [] pathDetails = new String [numEnd*2];
            g.dijkstra(startNodes[I]);
            for (int J = 0 ; J < numEnd ; J++)
            {
                String path = g.getPath(endNodes[J]);
                int index = path.indexOf(":");
                if (index != -1) {
                	pathDetails[2*J] = path.substring(0,index);
                	pathDetails[2*J+1] = path.substring(index+1);
                } else {
                	pathDetails[2*J] = Double.toString(INFINITY);
                	pathDetails[2*J+1] = "";
                }
            }
            arrPath[I]=pathDetails;
        }
        return arrPath;
    }
    
    private static String[][] createPathArray2(Graph g, int numStart, String[] startNodes, int numEnd, String[] endNodes) {
        String[][] arrPath  = new String [numStart][];
        for (int I = 0 ; I < numStart ; I++)
        {
            String [] pathDetails = new String [numEnd*2];
            g.dijkstra2(startNodes[I]);
            for (int J = 0 ; J < numEnd ; J++)
            {
                String path = g.getPath(endNodes[J]);
                int index = path.indexOf(":");
                if (index != -1) {
                	pathDetails[2*J] = path.substring(0,index);
                	pathDetails[2*J+1] = path.substring(index+1);
                } else {
                	pathDetails[2*J] = Double.toString(INFINITY);
                	pathDetails[2*J+1] = "";
                }
            }
            arrPath[I]=pathDetails;
        }
        return arrPath;
    }
}
