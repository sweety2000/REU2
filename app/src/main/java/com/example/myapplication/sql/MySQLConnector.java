package com.example.myapplication.sql;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.example.myapplication.shopping.ShoppingCart;
import com.mysql.cj.jdbc.AbandonedConnectionCleanupThread;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
import java.util.Scanner;

public class MySQLConnector {

    MySQLConnector() throws Exception {
        System.out.println("Loading application properties");
        Properties properties = new Properties();
        properties.load(MySQLConnector.class.getClassLoader().getResourceAsStream("application.properties"));

        System.out.println("Connection to the database");
        Connection connection = DriverManager.getConnection(properties.getProperty("url"), properties);
        System.out.println("Database connection test: " + connection.getCatalog());

        System.out.println("Create database schema");
        Scanner scanner = new Scanner(MySQLConnector.class.getClassLoader().getResourceAsStream("schema.sql"));
        Statement statement = connection.createStatement();

        while (scanner.hasNextLine()) {
            statement.execute(scanner.nextLine());
        }

        System.out.println("Closing database connection");
        connection.close();
        AbandonedConnectionCleanupThread.uncheckedShutdown();
    }

    private void insertData(@NonNull Connection connection) throws SQLException {
        System.out.println("Inserting data...");

        PreparedStatement statement = connection.prepareStatement("");
        statement.executeUpdate();
    }

    @Nullable
    private ShoppingCart readData(@NonNull Connection connection) throws SQLException {
        System.out.println("Reading data...");

        PreparedStatement statement = connection.prepareStatement("SELECT * FROM list;");
        ResultSet resultSet = statement.executeQuery();

        if (!resultSet.next()) {
            System.out.println("There is no data in the database!");
            return null;
        }
        ShoppingCart cart = new ShoppingCart();
        System.out.println("Data read from the database: " + cart.toString());
        return cart;
    }

    private void updateData(@NonNull Connection connection) throws SQLException {
        System.out.println("Updating data...");

        PreparedStatement update = connection.prepareStatement("");
        update.executeUpdate();

        readData(connection);
    }

    private void deleteData(@NonNull Connection connection) throws SQLException {
        System.out.println("Deleting data...");

        PreparedStatement delete = connection.prepareStatement("");
        delete.executeUpdate();

        readData(connection);
    }

}
