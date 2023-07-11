import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Routes, RouterModule } from '@angular/router';
import { PorfileComponent } from './components/porfile/porfile.component'; 

const routes: Routes = [
  { path: 'porfile', component: PorfileComponent },
];


@NgModule({
  declarations: [
    AppComponent,
    PorfileComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    AppRoutingModule
  ],
  exports:[RouterModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
