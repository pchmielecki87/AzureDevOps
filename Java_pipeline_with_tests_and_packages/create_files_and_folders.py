import os

# Define the project structure
project_name = "SimpleJavaApp"
directories = [
    f"./{project_name}/src/main/java/one/techbrain",
    f"./{project_name}/src/test/java/one/techbrain",
    f"./{project_name}/.azure-pipelines"
]

# Define file contents
pom_xml = """<project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
   <modelVersion>4.0.0</modelVersion>

   <groupId>one.techbrain</groupId>
   <artifactId>SimpleJavaApp</artifactId>
   <version>1.0-SNAPSHOT</version>
   <packaging>jar</packaging>

   <properties>
       <maven.compiler.source>1.8</maven.compiler.source>
       <maven.compiler.target>1.8</maven.compiler.target>
   </properties>

   <dependencies>
       <dependency>
           <groupId>org.junit.jupiter</groupId>
           <artifactId>junit-jupiter-api</artifactId>
           <version>5.7.0</version>
           <scope>test</scope>
       </dependency>
       <dependency>
           <groupId>org.junit.jupiter</groupId>
           <artifactId>junit-jupiter-engine</artifactId>
           <version>5.7.0</version>
           <scope>test</scope>
       </dependency>
   </dependencies>

   <build>
       <plugins>
           <plugin>
               <groupId>org.apache.maven.plugins</groupId>
               <artifactId>maven-compiler-plugin</artifactId>
               <version>3.8.1</version>
               <configuration>
                   <source>1.8</source>
                   <target>1.8</target>
               </configuration>
           </plugin>
           <plugin>
               <groupId>org.apache.maven.plugins</groupId>
               <artifactId>maven-surefire-plugin</artifactId>
               <version>2.22.2</version>
           </plugin>
       </plugins>
   </build>
</project>
"""

main_java = """package one.techbrain;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Azure DevOps!");
    }
}
"""

test_java = """package one.techbrain;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class MainTest {

    @Test
    public void testMain() {
        assertTrue(true);
    }

    @Test
    public void testAnother() {
        assertTrue(true);
    }

    @Test
    public void testMore() {
        assertTrue(true);
    }

    @Test
    public void testAdditional() {
        assertTrue(true);
    }

    @Test
    public void testYetAnother() {
        assertTrue(true);
    }
}
"""

pipeline_yaml = """trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UseJava@1
  inputs:
    versionSpec: '11'
    jdkArchitectureOption: 'x64'
    jdkSourceOption: 'PreInstalled'
    jdkVersionOption: '11'
    jdkArchitectureOption: 'x64'
    checkLatest: true

- task: Maven@3
  inputs:
    goals: 'clean package'

- task: PublishTestResults@2
  inputs:
    testResultsFormat: 'JUnit'
    testResultsFiles: '**/target/surefire-reports/TEST-*.xml'
    failTaskOnFailedTests: true

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(System.DefaultWorkingDirectory)/target/*.jar'
    ArtifactName: 'java-app-jar'
    publishLocation: 'Container'

- task: UniversalPackages@0
  inputs:
    command: 'publish'
    publishDirectory: '$(System.DefaultWorkingDirectory)/target'
    feedsToUse: 'internal'
    vstsFeedPublish: 'YourFeedName'
    vstsFeedPackagePublish: 'SimpleJavaApp'
    packagePublishDescription: 'SimpleJavaApp package'
"""

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with content
with open(f"./{project_name}/pom.xml", "w") as f:
    f.write(pom_xml)

with open(f"./{project_name}/src/main/java/one/techbrain/Main.java", "w") as f:
    f.write(main_java)

with open(f"./{project_name}/src/test/java/one/techbrain/MainTest.java", "w") as f:
    f.write(test_java)

with open(f"./{project_name}/.azure-pipelines/azure-pipelines.yml", "w") as f:
    f.write(pipeline_yaml)

print("Project structure and files created successfully!")
