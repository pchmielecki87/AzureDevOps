import os

# Define the directory structure
project_name = "SimpleJavaApp"
directories = [
    f"./{project_name}/src/main/java/com/example",
    f"./{project_name}/src/test/java/com/example",
    f"./{project_name}/.azure-pipelines"
]

# Define file contents
main_java = """
package com.example;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Azure DevOps!");
    }
}
"""

test_java = """
package com.example;

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

pipeline_yaml = """
trigger:
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

- script: |
    cd $(Build.SourcesDirectory)/src
    mkdir -p $(Build.ArtifactStagingDirectory)
    javac -d $(Build.ArtifactStagingDirectory)/classes $(Build.SourcesDirectory)/src/main/java/com/example/Main.java
    jar cvf $(Build.ArtifactStagingDirectory)/$(Build.BuildId).jar -C $(Build.ArtifactStagingDirectory)/classes .
  displayName: 'Compile Java Code'

- script: |
    cd $(Build.SourcesDirectory)/src
    javac -cp $(Build.ArtifactStagingDirectory)/classes:. $(Build.SourcesDirectory)/src/test/java/com/example/MainTest.java
    java -cp $(Build.ArtifactStagingDirectory)/classes:$(Build.SourcesDirectory)/src/test/java:$(Build.SourcesDirectory)/lib/junit-5.7.1.jar org.junit.runner.JUnitCore com.example.MainTest
  displayName: 'Run Tests'

- task: PublishPipelineArtifact@1
  inputs:
    targetPath: $(Build.ArtifactStagingDirectory)
    artifact: drop
    publishLocation: 'pipeline'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId).jar'
    ArtifactName: 'java-app-jar'
    publishLocation: 'Container'
"""

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files with content
with open(f"./{project_name}/src/main/java/com/example/Main.java", "w") as f:
    f.write(main_java)

with open(f"./{project_name}/src/test/java/com/example/MainTest.java", "w") as f:
    f.write(test_java)

with open(f"./{project_name}/.azure-pipelines/azure-pipelines.yml", "w") as f:
    f.write(pipeline_yaml)

print("Project structure created successfully!")
